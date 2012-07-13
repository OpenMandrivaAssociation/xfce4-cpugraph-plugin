%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	CPU Graph plugin for the Xfce panel
Name:		xfce4-cpugraph-plugin
Version:	1.0.5
Release:	1
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpugraph-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-cpugraph-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfcegui4-devel
Obsoletes:	xfce-cpugraph-plugin

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

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/xfce4/panel-plugins/*
%{_iconsdir}/hicolor/*/apps/*.png
