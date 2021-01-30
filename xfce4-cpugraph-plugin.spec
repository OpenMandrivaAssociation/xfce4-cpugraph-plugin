%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	CPU Graph plugin for the Xfce panel
Name:		xfce4-cpugraph-plugin
Version:	1.2.1
Release:	1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpugraph-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-cpugraph-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
BuildRequires:	xfce4-dev-tools
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)

%description
xfce4-cpugraph-plugin is a panel plugin for Xfce panel.
It shows a graph of your latest system load.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*
%{_iconsdir}/hicolor/*/apps/*.png
