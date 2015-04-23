Summary: 	Shared files for the Matchbox Desktop
Name: 		matchbox-common
Version: 	0.9.1
Release: 	7
Url: 		http://matchbox.handhelds.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://matchbox-project.org/sources/%{name}/0.9/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libmb)
BuildArch:	noarch

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains graphics and scripts required by Matchbox.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc ChangeLog
%_bindir/matchbox-session
%_datadir/matchbox
%_datadir/pixmaps/*
%_iconsdir/blondie
