Name:       sodesk 
Version:    1.1.9
Release:    0
Summary:    RPM package
License:    GPL-3.0
Requires:   gtk3 libxcb1 xdotool libXfixes3 alsa-utils curl libXtst6 libayatana-appindicator3-1 libvdpau1 libva2

%description
The best open-source remote desktop client software, written in Rust. 

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/sodesk/
mkdir -p %{buildroot}/usr/share/sodesk/files/
install -m 755 $HBB/target/release/sodesk %{buildroot}/usr/bin/sodesk
install $HBB/libsciter-gtk.so %{buildroot}/usr/lib/sodesk/libsciter-gtk.so
install $HBB/res/sodesk.service %{buildroot}/usr/share/sodesk/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/sodesk/files/sodesk.png
install $HBB/res/sodesk.desktop %{buildroot}/usr/share/sodesk/files/
install $HBB/res/sodesk-link.desktop %{buildroot}/usr/share/sodesk/files/

%files
/usr/bin/sodesk
/usr/lib/sodesk/libsciter-gtk.so
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
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac
