### Updates

*2018-12-18.1* - Break has been good, on top of updates right now.
Finally got some housekeeping done and whipped package licenses into shape again, properly.
Also added some stuff so builds by default don't rebuilt current packages.
I still see the need to someday cull run/build deps and redo all of that stuff.
Also, some of the things pulled in for the Golang bits have probably changed, need to cull.
I also need to redo my scripts to be sane and unified - as is, I keep adding more of them with little purpose.

***

*2018-11-13.1* - University is still super busy, but Christmas break should see some more work on this.
I have a desktop now, so compiling isn't too much of a pain, I can just leave it going when I'm away.
Still have the backlog of upgrades to clear out though.

***

*2018-10-06.1* - University is super busy, I am really not able to put much time into this, which is fine - I knew that'd happen.
Happened to have a free Friday night that I wanted to space out, so some upgrades are being pushed through.

***

*2018-08-13.1* - More updates, more testing being done, same as usual.
Preparing to head off to University, so time for this isn't guaranteed (like it ever was...)

***

*2018-08-07.1* - Plenty of updates, more testing being done, things seem to be building okay again for now.
Will probably have less time for this soon, going to University middle of this month.

***

*2018-07-23.2* - Everything finally build correctly!
Will try installing on bare metal again after... well over a month.

***

*2018-07-23.1* - Another day, another update.
`deepin-daemon` is building again, I think an upgrade fixed it.
Hopefully moving back to a functioning build.

***

*2018-07-20.1* - Well, as you can guess, I didn't get `deepin-daemon` working.
Might have a lead, we'll see.
Been busy with... life, I guess.
Anyway, a fresh round of upstream updates, hoping they'll fix my issues and get building again.
As is, I've not been running Deepin as my main desktop for over a month.
Also, `cr.deepin.io` is down, so that's stopping me right now.

***

*2018-07-01.1* - Finished the gig out of state, back home until this afternoon.
Finally realized why `deepin-qt5dxcb-plugin` wasn't building, it was `qt5-xcb-private-headers` being out of date.
`deepin-daemon` on the other hand still seems to be failing, but I have a sneaking suspicion it's something similar.

***

*2018-06-24.1* - Been a while, not a whole lot to do here, and been flat out working (child care).
Short story short, upstream changes are keeping `deepin-daemon` and `deepin-qt5dxcb-plugin` from building, so the whole stack is at a standstill right now until either upstream Deepin fixes things to work with newer software, or I can find a fix somewhere.
I need to submit a bug report, but I'm not sure what bit changed to make things break, so it's hard to do right now.

***

*2018-06-07.3* - Calling it quits for today, I need to pack and go to bed. 

***

*2018-06-07.2* - Trying to rebuild/upgrade, but `deepin-daemon` is now broken due to other upstream upgrades (previous good builds now fail).
We'll see... I will be busy for the next few days at least.

***

*2018-06-07.1* - So, after all this time, I've finally gotten internet shared across... Just in time to leave for a month, starting tomorrow.
Should hopefully have internet to work with while away though.

***

*2018-05-30.3* - All rebuilt, seems okay thus far.
Nice to see things are moving forward.

***

*2018-05-30.2* - The moral of the story - git tags can be changed...
So was getting build errors because a tag had been quickly reassigned to a fixed commit, but I had the old tag, so solbuild doesn't think it needs to check anything.

***

*2018-05-30.1* - Updates are out there.
Last time, I tried updating things, builds failed, but I think I'm getting there now.
Once I have better internet, I'll be able to do things proper.
And yes, better internet is in the works at least...

***

*2018-05-19.3* - Only issue so far was with Deepin Terminal, which Arch had a patch for (thanks!) - all good now.

***

*2018-05-19.2* - Okay, all rebuilt, will test updates now.
Wish me luck...

***

*2018-05-19.1* - All quiet on the update front, and I'm somewhere with good internet right now, so I'm pushing to get things whipped into shape.
Fingers crossed, none of the changes require too much to sort out.

***

*2018-05-14.1* - Yup, even more updates, which is pretty cool.
Looking forward to getting all of this sorted again, but I can't do so for a little while.

***

*2018-05-13.2* - As I suspected, there are a ton more updates that are rolling out, so I'm going to let the churn settle before I touch this (I don't want to break my own desktop, after all).
Overall, I'm way more impressed with how quickly updates are done with Deepin compared to Gnome...

***

*2018-05-13.1* - A slew of updates are out there, but... Don't have the time to do the upgrades on my slow internet right now.
Maybe later.
I have them ready to build though.

***

*2018-05-11.1* - Upstream put out a point release for `deepin-qt5dxcb-plugin`, so that builds now.
A couple other package updates as well.
For now, unless there's an ABI or other file change, I'll hold off rebuilding (unless I see things are broken, or it's a non-ABI dependant situation, such as `deepin-gir-generator`, etc.).

***

*2018-05-06.1* - Well, I upgraded packages, reinstalled my Deepin packages.
So far, so good... Woot?

***

*2018-05-05.3* - Finally updated and rebuilt all my packages, now to upgrade my system, and then I'll try for a reboot.
All of that can wait for tomorrow.

***

*2018-05-05.2* - Things are nearly done in this round of upgrades.
Would have been a lot quicker if I had better internet...
Oh well.

As explaination, I'm without any fixed line internet, have to use mobile for now.
I get 2GB/month, with about 15KB/s unlimited thereafter.
Well, you can see why it takes a while.
Hopefully, I'll be getting internet shared across from neighbors soon enough.

***

*2018-05-05.1* - Found a fix in master for `dtkwidget`, but the latest version of `deepin-qt5dxcb-plugin` is still borked.
Taking a while, but I'm working on rebuilds (and updating my install of Solus), then we'll try for a reboot and see what happens.

***

*2018-05-04.1* - Updates are being a bitch...
We'll see.
Would be a lot easier with better internet, which *might* happen soonish.

***

*2018-04-29.1* - I'm almost mad, I wish I'd found this sooner - [an official dependancy graph](https://salsa.debian.org/pkg-deepin-team/progress-tracker/blob/master/depgraph/pkg-deepin-dep.svg) from Deepin.
Once I have good internet, I'll go through all packages, cut deps *wayyyy* back, and re-add them as shown.

***

*2018-04-26.2* - I went ahead and am running the current build now.
User icons are gone (?).
For now, fudging things by removing lightdm and replacing with gdm.
I would remove the dependancy between `liblightdm-qt5` and `lightdm`, but that wouldn't be correct, and this is just a short term measure anyway.

***

*2018-04-26.2* - Got my rebuilds done (at last - I'm on a throttled connection).
Not a lot happening on my end until I can test with updates from Solus, once those come out.

***

*2018-04-26.1* - Okay, almost all on upstream git now (just wallpapers left iirc), but things are iffy.
I believe that having rebuilt packages, they rely on Solus updates that are not yet safe to apply (specifically, `lightdm` is borked as far as I can tell).
So, installing `gdm` was enough as a stopgap measure for my Deepin machine to keep it limping along, but it also uninstalled some stuff...

But, of course, `cr.deepin.io` would go down as I try to do rebuilds, wouldn't it...

***

*2018-04-24.1* - Doing the final spree of moving over to upstream git, worked out what's wrong with `deepin-image-viewer` (`freeimage` needed to rebuild, upstream had changed between the two).

***

*2018-04-22.1* - I *would* be working on things, but the SSL cert on the Deepin [dev site](https://cr.deepin.io/) is expired, so building is a no-go until that's resolved.

***

*2018-04-20.1* - Been working through packages, switching from GitHub sources to use upstream git sources (the GH mirrors seem to be frozen at the moment, since about a week ago).
This has the added benefit to me of reducing download overhead when I next upgrade packages, as the majority of the source is going to remain the same.
A few updates are being picked up along the way.

***

*2018-04-15.1* - Just a few updates, nothing big as far as I can tell.
`deepin-image-viewer` stopped building with the latest update to 1.2.19, so I need to sort that out. 

***

*2018-04-05.1* - Got Deepin Movie (Reborn) packaged up, I really like it (for the most part, see further).
Tried it in a VM, it doesn't work solo at this point.
I suspect it's something to do with not having acceleration available.
Will test on bare metal soon(ish?).

Some points against it though:

* it does not support letterboxing when in windowed mode (meaning no split screen viewing, unless your content happens to be a vertical format)
* it does not support any cropping modes, so no trimming off baked letterboxes

***

*2018-04-03.1* - Got a few updates done (was busy over the weekend, and it wasn't urgent, so...), things should be up to date again.
I find a few random application crashes now and again, need to determine if it's to do with my building of the DE (probably not), the DE itself (maybe), or the apps in particular (more likely).

***

*2018-03-26.2* - Did a full rebuild with my scripts, ironed out the last of the run/build_dep file issues.
Also sorted out which apps run solo (and made sure they had the right rundeps), and *started* on a bit of making sure lower level components actually have the rundeps they need (`deepin-daemon` so far has been tested a little)

***

*2018-03-26.1* - Things are going to slow down now, reasons being:
* I've gotten the main desktop done, it's mainly peripheral apps now. If updates come out, I'll try to make sure I upgrade and all that.  
* I'm going to be busy (getting a job), I won't have a ton of time to dump into this. Make no promises, tell no lies, aye?
* Internet isn't real good for me where I'm at now, it'll be a few months before that might change for the long run.

I am running this desktop fully at the moment, so I *am* testing it through use, but it also means I might not catch corner-case features that I don't know about.
This project is for me after all, I only feel motivated about what's important to me.

***

*2018-03-25.1* - Redid a lot of my build script to work correctly.
Opted to force `LIB_INSTALL_DIR` and `PREFIX` on all similar Deepin packages, even if they don't *strictly* need it.
Having done that has fixed an issue with the dock not finding a file for the power menu.

***

*2018-03-24.2* - Got my build script set up, should now help insulate me from accidentally inheriting deps that are not in my lists.
Will in due course rebuild all packages to validate my run/build_dep files.
For now though, I've updated everything!

***

*2018-03-24.1* - Gone back through all my packages, spent way too long fighting `treefrog-framework`, but have no un-commited files or changes now.
Will start upgrading more things in the morning...  
Some things of note:
* If I don't include a rundep that the arch repos do, it's because I can't see why I need it. I will slowly try to add these back in as I determine why I need them
* All things considered, the desktop is running really well. Niggling issues include:
  * ~~~Dock power menu does not work, can't see why (that is, the error message says it can't find a file that I think exists)~~~
  * Dock/Launcher/Control Center are sporadic about HiDPI support when launched by startdde (that is, at login). If manually launched from the terminal, they're fine. Need to investigate what flags might cause that.

***

*2018-03-23.1* - Still more combing through.
Trying to make sure `startdde` has all the correct deps to run the DE.
Mostly working?
Running under a VM to test stock has issues since window manager stuff gets knocked about for the sake of performance (and perhaps rightly so, but still).

***

*2018-03-22.1* - Combing back through with a locked set of packages (there are some updates floating out there - I'm leaving them until I rebuild the whole stack).
Have pretty much made sure the current (normally working, i.e - not the image viewer) desktop apps have all the correct deps to run solo.

***

*2018-03-21.2* - So, yeah, I got the critical bits in to make things run now.
[M'pics](https://imgur.com/a/LoZGW).
Key bit was `deepin-qt5dxcb-plugin` to tie things together.
Confusing name meant I kept overlooking it for a long time.

***

*2018-03-21.1* - I've been working through, trying to get a functioning desktop.
Takes a while though...

***

*2018-03-10.1* - I've sorta gotten past the point of needing to watch the Arch repos, so maybe I'll do more here?
Thinking I'll be ironing things out, package by package (i.e. Terminal and all deps, file manager and all deps, etc.)
Ideally, I will keep rundeps to a minumum, since someone might only want one app.

***

*2018-03-05.1* - I poked some more, got past some issues, still stuck on some things.

***

*2018-03-01.1* - I tried poking at this some more, but Arch is lagging upstream and I can't be bothered to work on this too much. The effort of attempting to build *and update* and desktop stack at the same time is beyond me.
Maybe someday...
