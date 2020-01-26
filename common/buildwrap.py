#!/usr/bin/env python

#
#  USAGE: buildwrap.py start|stop|restart -d
#
#  This requires the following sudo rule (change "ikey" for your username)
#       Cmnd_Alias BOT_CMDS = /usr/bin/evobuild
#       ikey ALL=(ALL) NOPASSWD: BOT_CMDS
#
#  Copyright 2015 Ikey Doherty <ikey@solus-project.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import os
import commands
import sys

if "-d" in sys.argv:
    from daemon import runner
import time
import shutil
import subprocess
import shlex
import glob

WorkDir = "/BUILDDIR"
SSH_HOST = "getsol.us"
BASE_REPO = "ssh://vcs@dev.getsol.us:2222/source"

targetRepo = "unstable"


def check_output(cmd):
    return subprocess.check_output(shlex.split(cmd))

class Builder():

    def __init__(self):
        self.pidfile_path =  '%s/build.pid' % WorkDir
        self.pidfile_timeout = 5
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'

        self.wd = os.getcwd()

    def report_status(self, id, status):
        try:
            os.system("ssh -p 798 -4 build@%s status %s %s" % (SSH_HOST, id, status))
        except Exception, e:
            print e
            sys.exit(-1)

    def run(self):
        while True:
            # attempt to get a job. :P
            os.chdir(self.wd)
            output = None
            try:
                output = check_output("ssh -p 798 -4 build@%s get" % SSH_HOST)
            except Exception, e:
                time.sleep(10)
                continue
            if "\t" not in output:
                time.sleep(10)
                continue

            splits = output.split("\t")
            id = splits[0].replace("\n","")
            pkg = splits[1].replace("\n","")
            tag = splits[2].replace("\n","")
            print "Taking: %s %s" % (pkg, tag)

            clone_uri = "%s/%s.git" % (BASE_REPO, pkg)

            clone_dir = os.path.join(WorkDir, "CLONE", pkg)
            clone_base = os.path.join(WorkDir, "CLONE")
            if os.path.exists(clone_dir):
                try:
                    shutil.rmtree(clone_dir)
                except Exception, e:
                    self.report_status(id, "FAILED")
                    time.sleep(10)
                    continue

            try:
                if not os.path.exists(clone_base):
                    os.makedirs(clone_base)
            except Exception, e:
                print e
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            clcmd = "git clone -b {} --depth 20 --single-branch {}"
            wd = os.getcwd()
            try:
                os.chdir(clone_base)
                check_output(clcmd.format(tag, clone_uri))
            except Exception, e:
                print e
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            yml = os.path.abspath(os.path.join(clone_dir, "package.yml"))
            spec = os.path.abspath(os.path.join(clone_dir, "pspec.xml"))
            tgt = None
            if os.path.exists(yml):
                tgt = yml
            elif os.path.exists(spec):
                tgt = spec
            else:
                print("Cannot determine package type")
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            builddir = os.path.join(WorkDir, "BUILD")
            if os.path.exists(builddir):
                try:
                    shutil.rmtree(builddir)
                except Exception, e:
                    print("Cannot remove tree")
                    self.report_status(id, "FAILED")
                    time.sleep(10)
                    continue

            try:
                os.makedirs(builddir)
            except Exception, e:
                print("Cannot create tree")
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            os.chdir(builddir)
            cmd = "sudo solbuild -d --transit-manifest %s -n build %s -p unstable-x86_64 > \"%s.log\" 2>&1" % (targetRepo, tgt, tag)
            self.report_status(id, "BUILDING")
            r = 0
            try:
                r = os.system(cmd)
            except Exception, e:
                print e
                sync_logs(tag, True)
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            # build failure.
            if r != 0:
                sync_logs(tag, True)
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            pkgs = None
            try:
                f = glob.glob("*.eopkg")
                pkgs = [os.path.basename(x) for x in f]
            except Exception, e:
                print e
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            trams = None
            try:
                f = glob.glob("*.tram")
                trams = [os.path.basename(x) for x in f]
            except Exception, e:
                print e
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            if len(pkgs) < 1:
                sync_logs(tag, True)
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            # Should only ever have *1* .tram file
            if len(trams) != 1:
                sync_logs(tag, True)
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            try:
                check_output("scp -4 -P 798 %s %s ferryd@%s:root/incoming" % (" ".join(pkgs), trams[0], "ring0.solus-project.com"))
            except Exception, e:
                print e
                self.report_status(id, "FAILED")
                time.sleep(10)
                continue

            sync_logs(tag)

            # technically finished?
            self.report_status(id, "OK")
            time.sleep(10)

def sync_logs(tag, skip=False):
    try:
        check_output("gzip \"%s.log\"" % tag)
        check_output("scp -4 -P 798 \"%s.log.gz\" logs@%s:logs/." % (tag, SSH_HOST))
    except Exception, e:
        print e
        if not skip:
            self.report_status(id, "FAILED")
            time.sleep(10)

if __name__ == "__main__":
    app = Builder()
    if "-d" in sys.argv:
        run = runner.DaemonRunner(app)
        run.do_action()
    else:
        app.run()
