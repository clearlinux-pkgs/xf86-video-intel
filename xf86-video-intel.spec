#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86-video-intel
Version  : 1
Release  : 34
URL      : https://cgit.freedesktop.org/xorg/driver/xf86-video-intel/snapshot/dad64e9f76c718033402be7bfd2129866d492304.tar.gz
Source0  : https://cgit.freedesktop.org/xorg/driver/xf86-video-intel/snapshot/dad64e9f76c718033402be7bfd2129866d492304.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-intel-lib
Requires: xf86-video-intel-bin
Requires: xf86-video-intel-doc
Requires: xf86-video-intel-data
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-xlib-xrender)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(presentproto)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb-aux)
BuildRequires : pkgconfig(xcb-dri2)
BuildRequires : pkgconfig(xcb-dri3)
BuildRequires : pkgconfig(xcb-present)
BuildRequires : pkgconfig(xcb-sync)
BuildRequires : pkgconfig(xcb-xfixes)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xf86driproto)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xfont)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xrender)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xtst)
BuildRequires : pkgconfig(xvmc)
BuildRequires : pkgconfig(xxf86vm)
BuildRequires : xscreensaver
Patch1: 0001-uxa-Ensure-we-include-headers-for-stat.patch
Patch2: use-O3.patch

%description
xf86-video-intel
Open-source X.org graphics driver for Intel graphics
https://01.org/linuxgraphics/

%package bin
Summary: bin components for the xf86-video-intel package.
Group: Binaries
Requires: xf86-video-intel-data

%description bin
bin components for the xf86-video-intel package.


%package data
Summary: data components for the xf86-video-intel package.
Group: Data

%description data
data components for the xf86-video-intel package.


%package dev
Summary: dev components for the xf86-video-intel package.
Group: Development
Requires: xf86-video-intel-lib
Requires: xf86-video-intel-bin
Requires: xf86-video-intel-data
Provides: xf86-video-intel-devel

%description dev
dev components for the xf86-video-intel package.


%package doc
Summary: doc components for the xf86-video-intel package.
Group: Documentation

%description doc
doc components for the xf86-video-intel package.


%package lib
Summary: lib components for the xf86-video-intel package.
Group: Libraries
Requires: xf86-video-intel-data

%description lib
lib components for the xf86-video-intel package.


%prep
%setup -q -n dad64e9f76c718033402be7bfd2129866d492304
%patch1 -p1
%patch2 -p1

%build
export LANG=C
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%autogen --disable-static --with-default-accel=sna --enable-uxa --enable-sna --enable-dri3 --with-default-dri=3
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/xf86-video-intel-backlight-helper

%files data
%defattr(-,root,root,-)
/usr/share/polkit-1/actions/org.x.xf86-video-intel.backlight-helper.policy

%files dev
%defattr(-,root,root,-)
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/xorg/modules/drivers/intel_drv.so
