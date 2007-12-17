%define name 	matchbox-common
%define version 0.9.1
%define release %mkrel 2

Summary: 	Shared files for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox.handhelds.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/%{name}/0.9/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig libmatchbox-devel
BuildArch:	noarch

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains graphics and scripts required by Matchbox.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%_bindir/matchbox-session
%_datadir/matchbox
%_datadir/pixmaps/*
%_iconsdir/blondie
