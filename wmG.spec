Summary:	A small, lightweight GNOME window manager
Summary(pl):	Ma³y zarz±dca okien do GNOME
Name:		wmG
Version:	0.14.8
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	http://www.ductape.net/~reeve/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	b3e5b3a2e65bc44cca40d80a8485392e
Source1:	%{name}-xsession.desktop
URL:		http://www.ductape.net/~reeve/projects.html#wmG
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	libstdc++-devel
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
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	wmdatadir=%{_wmpropsdir}

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_wmpropsdir}/*
%{_datadir}/xsessions/%{name}.desktop
