%define name 	matchbox-common
%define version 0.9.1
%define release %mkrel 6

Summary: 	Shared files for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox.handhelds.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-6mdv2011.0
+ Revision: 620296
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.1-5mdv2010.0
+ Revision: 429958
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-4mdv2009.0
+ Revision: 251939
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Mon Nov 05 2007 Funda Wang <fwang@mandriva.org> 0.9.1-2mdv2008.1
+ Revision: 105981
- Rebuild
- import matchbox-common


* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 0.9.1-1mdk
- 0.9.1

* Tue Jan 4 2005 Austin Acton <austin@mandrake.org> 0.9-1mdk
- 0.9

* Mon Jul 20 2004 Austin Acton <austin@mandrake.org> 0.8-1mdk
- 0.8

