Summary:	A small, lightweight GNOME window manager.
Name:		wmG
Version:	0.14.8
Release:	1
License:	GPL
Group:		X11/Window Managers
Source:		wmG-0.14.8.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_wmpropsdir	%{_datadir}/wm-properties

%description
wmG is a GNOME-compliant minimalistic window manager for X.

%prep
%setup -q
%build
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
