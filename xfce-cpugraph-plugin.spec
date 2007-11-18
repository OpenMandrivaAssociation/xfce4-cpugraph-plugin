Summary:	CPU Graph plugin for the Xfce panel
Name:		xfce-cpugraph-plugin
Version:	0.3.0
Release:	%mkrel 5
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cpugraph-plugin
Source0:	xfce4-cpugraph-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-cpugraph
Provides:	xfce-cpugraph
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A panel plugin for Xfce panel.
It shows a graph of your latest system load.

%prep
%setup -qn xfce4-cpugraph-plugin-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded devel files
#rm -f %{buildroot}/%{_libdir}/xfce4/panel-plugins/libcpugraph.a 

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO 
%{_libdir}/xfce4/panel-plugins/
%{_datadir}/xfce4/panel-plugins/*
