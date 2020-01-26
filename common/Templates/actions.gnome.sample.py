#!/usr/bin/python

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())


def setup():
    autotools.configure("--disable-static")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #EXTRADOCS#
