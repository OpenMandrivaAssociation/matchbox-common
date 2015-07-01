Summary: 	Shared files for the Matchbox Desktop
Name: 		matchbox-common
Version: 	0.9.1
Release: 	8
Url: 		http://matchbox.handhelds.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://matchbox-project.org/sources/%{name}/0.9/%{name}-%{version}.tar.bz2
Source1:	session
Patch0:		matchbox-session-good.patch
Requires:	dbus-x11

BuildRequires:	pkgconfig(libmb)
BuildArch:	noarch

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains graphics and scripts required by Matchbox.

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall
mkdir -p %{buildroot}%{_sysconfdir}/matchbox/
install -m0755 %{SOURCE1} %{buildroot}/%{_sysconfdir}/matchbox/

%files
%doc ChangeLog
%{_sysconfdir}/matchbox/session
%_bindir/matchbox-session
%_datadir/matchbox
%_datadir/pixmaps/*
%_iconsdir/blondie
