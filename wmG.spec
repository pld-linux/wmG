Summary: A small, lightweight GNOME window manager.
Name: wmG
Version: 0.14.8
Release: 1
Copyright: GPL
Group: "User Interface/Window Managers"
Source: wmG-0.14.8.tar.gz
Buildroot: /var/tmp/wmG-root/

%description
wmG is a GNOME-compliant minimalistic window manager for X.

%prep
%setup -q

%build
configure --prefix=$RPM_BUILD_ROOT/usr
make

%install
export PATH=/sbin:$PATH
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
/usr/bin/wmG
/usr/bin/wmGconf
/usr/share/gnome/wm-properties/wmG.desktop

%changelog
