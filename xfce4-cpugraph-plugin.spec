Summary:	CPU Graph plugin for the Xfce panel
Name:		xfce4-cpugraph-plugin
Version:	0.4.0
Release:	%mkrel 8
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpugraph-plugin
Source0:	%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-cpugraph-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
xfce4-cpugraph-plugin is a panel plugin for Xfce panel.
It shows a graph of your latest system load.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO 
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/xfce4/panel-plugins/*
