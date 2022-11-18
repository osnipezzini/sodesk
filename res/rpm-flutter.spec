Name:       sodesk 
Version:    1.2.0
Release:    0
Summary:    RPM package
License:    GPL-3.0
Requires:   gtk3 libxcb libxdo libXfixes pipewire alsa-lib curl libappindicator-gtk3 libvdpau libva
Provides:   libdesktop_drop_plugin.so()(64bit), libdesktop_multi_window_plugin.so()(64bit), libflutter_custom_cursor_plugin.so()(64bit), libflutter_linux_gtk.so()(64bit), libscreen_retriever_plugin.so()(64bit), libtray_manager_plugin.so()(64bit), liburl_launcher_linux_plugin.so()(64bit), libwindow_manager_plugin.so()(64bit), libwindow_size_plugin.so()(64bit)

%description
The best open-source remote desktop client software, written in Rust. 

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

# %global __python %{__python3}

%install

mkdir -p "%{buildroot}/usr/lib/sodesk" && cp -r ${HBB}/flutter/build/linux/x64/release/bundle/* -t "%{buildroot}/usr/lib/sodesk"
mkdir -p "%{buildroot}/usr/bin"
install -Dm 644 $HBB/res/sodesk.service -t "%{buildroot}/usr/share/sodesk/files"
install -Dm 644 $HBB/res/sodesk.desktop -t "%{buildroot}/usr/share/sodesk/files"
install -Dm 644 $HBB/res/sodesk-link.desktop -t "%{buildroot}/usr/share/sodesk/files"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/sodesk/files/sodesk.png"

%files
/usr/lib/sodesk/*
/usr/share/sodesk/files/sodesk.service
/usr/share/sodesk/files/sodesk.png
/usr/share/sodesk/files/sodesk.desktop
/usr/share/sodesk/files/sodesk-link.desktop

%changelog
# let's skip this for now

# https://www.cnblogs.com/xingmuxin/p/8990255.html
%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop sodesk || true
  ;;
esac

%post
cp /usr/share/sodesk/files/sodesk.service /etc/systemd/system/sodesk.service
cp /usr/share/sodesk/files/sodesk.desktop /usr/share/applications/
cp /usr/share/sodesk/files/sodesk-link.desktop /usr/share/applications/
ln -s /usr/lib/sodesk/sodesk /usr/bin/sodesk 
systemctl daemon-reload
systemctl enable sodesk
systemctl start sodesk
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop sodesk || true
    systemctl disable sodesk || true
    rm /etc/systemd/system/sodesk.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/share/applications/sodesk.desktop || true
    rm /usr/share/applications/sodesk-link.desktop || true
    rm /usr/bin/sodesk || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
