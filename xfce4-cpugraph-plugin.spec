%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	CPU Graph plugin for the Xfce panel
Name:		xfce4-cpugraph-plugin
Version:	1.0.5
Release:	2
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpugraph-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-cpugraph-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4ui-1)

%description
xfce4-cpugraph-plugin is a panel plugin for Xfce panel.
It shows a graph of your latest system load.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*
%{_iconsdir}/hicolor/*/apps/*.png


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.0.1-4mdv2012.0
+ Revision: 791552
- Rebuild
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.1-2
+ Revision: 790049
- Rebuild for 4.8.0

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1
+ Revision: 632777
- update to new version 1.0.1
- package new icons

* Sun Oct 03 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 582770
- update to new version 1.0.0
- tune up buildrequires
- update url for source 1
- corrent the docs files

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-8mdv2010.1
+ Revision: 543421
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.4.0-7mdv2010.0
+ Revision: 445980
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-6mdv2009.1
+ Revision: 349448
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-5mdv2009.1
+ Revision: 294991
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-4mdv2009.0
+ Revision: 262355
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-3mdv2009.0
+ Revision: 256837
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- better description

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Nov 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-1mdv2008.1
+ Revision: 111402
- package translation files
- new version

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-5mdv2008.1
+ Revision: 110114
- use tarball name as a real name
- correct buildrequires
- do not package COPYING and INSTALL files
- use upstream name

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-5mdv2008.0
+ Revision: 33222
- spec file clean
- update url

