Summary:	A small, lightweight GNOME window manager.
Summary(pl):	Maly GNOME window manager.
Name:		wmG
Version:	0.14.8
Release:	2
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz�dcy Okien
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
wmG is a GNOME-compliant minimalistic window manager for X.

%description -l pl
wmG jest zgodnym z GNOME minimalistycznym window manadzerem dla X.

%prep
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	wmdatadir=%{_wmpropsdir}

gzip -9nf AUTHORS COPYING ChangeLog NEWS README

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,COPYING,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_wmpropsdir}/*
