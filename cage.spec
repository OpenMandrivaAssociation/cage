Name:	cage
Version:	0.3.1
Release:        1
Summary:	A wayland kiosk to run a single maximized application
Group:	Wayland
License:	MIT
URL:	https://www.hjdskes.nl/projects/cage/
Source0:	https://github.com/cage-kiosk/cage/archive/refs/tags/v0.3.0.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wlroots-0.20)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xwayland)
BuildRequires:	scdoc

BuildSystem:	meson

%description
%{summary}.

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
