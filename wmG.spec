Summary:	A small, lightweight GNOME window manager
Summary(pl):	Ma³y zarz±dca okien do GNOME
Name:		wmG
Version:	0.14.8
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.ductape.net/~reeve/downloads/%{name}-%{version}.tar.gz
URL:		http://www.ductape.net/~reeve/projects.html#wmG
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_wmpropsdir	/usr/share/wm-properties

%description
wmG is a GNOME-compliant minimalistic window manager for X.

%description -l pl
wmG jest zgodnym z GNOME minimalistycznym zarz±dc± okien dla X.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	wmdatadir=%{_wmpropsdir}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_wmpropsdir}/*
