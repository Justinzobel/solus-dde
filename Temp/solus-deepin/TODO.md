### TODO

**Apps that run on an otherwise stock Solus (Budgie) install**

- [x] Calculator
- [x] Calendar (though it's pretty much useless)
- [ ] Editor (Need to test)
- [x] File Manager
- [x] Image Viewer
- [x] Movie (VM lacks the correct acceleration I believe, works fine bare metal)
- [x] Music
- [ ] Picker (may not be possible?)
- [ ] Screen Recorder (may not be possible?)
- [x] Screenshot
- [x] System Monitor
- [x] Terminal
- [x] Voice Recorder



***

#### `deepin-daemon`

Look into packaging Miracast/Miracle Cast - [Tarball](https://github.com/linuxdeepin/miraclecast/archive/1.0.8.tar.gz)

Currently stuck with:
```
/home/build/YPKG/root/deepin-miraclecast/build/miraclecast-1.0.8/res/dispctl.vala:807.2-807.18: error: 1 missing arguments for `void GLib.Application.set_default (GLib.Application?)'
	app.set_default();
	^^^^^^^^^^^^^^^^^
Compilation failed: 1 error(s), 2 warning(s)
```

Will try with upstream `miraclecast` and hopefully it'll work.

Add as rundep:
* `imwheel` (used for mouse wheel settings)
* `rfkill` (used with Bluetooth)

Look into:
* missing files from `/usr/share/deepin-default-settings`, see `deepin-default-settings`.
* `deepin-polkit-agent-ext-gnomekeyring` [git source](https://cr.deepin.io/admin/projects/dpa-ext-gnomekeyring)

#### `deepin-desktop`

Known tasks:
* Rundeps are mixed up - startdde is probably what wants many of these, desktop is just one of them. This falls under the general mucking out of rundeps that needs to go on.

#### `deepin-dock` / `deepin-launcher`

Need to investigate:
* using a different icon theme does not change immediately (possibly only when HIDPI is working?)

#### `deepin-editor`

Need to investigate:
```
No appenders assotiated with category org.kde.ksyntaxhighlighting
[Error  ] <> Repository got deleted while a highlighter is still active!
```

#### `deepin-file-manager`

Look into packaging:
* [dde-file-manager-integration](https://cr.deepin.io/admin/projects/dde/dde-file-manager-integration)
* dde-file-dialog-gtk

Need to investigate:
* cannot mount MTP Android device (can only test with Samsung Galaxy S5 currently, but that works under GNOME)

Known tasks:
* `/usr/bin/dde-xdg-user-dirs-update` is not executable. Need to see why and possibly remedy that (as it's a script, it may be run via bash, instead of directly).

#### `deepin-image-viewer`

It breaks Krita (amongst other things, probably).
This has been known to upstream for some time.
I also doesn't build right now, due to upstream Solus changes to Freeimage.

#### `deepin-qt5config`

[What is it?](https://cr.deepin.io/#/admin/projects/deepin-qt5config)
Do I need it? Probably, right?

#### `startdde`

Look into:
* `startmanager.go:90: open /usr/lib/UIAppSched.hooks/launched: no such file or directory`

#### Misc.

* validate core packages and strip un-needed rundeps (and add those that are required). This one is hard though, we'll see.
* check if `deepin-music` is using vendored libraries and transition off of them if possible.
* check on how to make sure `setcap cap_kill,cap_net_raw,cap_dac_read_search,cap_sys_ptrace+ep /usr/bin/deepin-system-monitor` is run so that network speed monitoring may be achieved.
* investigate why first login (at least in VM) has a white bg, as you have to fish for a button.
* `deepin-movie` has 'volume down' when it should have 'Volume down', in keyboard shortcuts.
