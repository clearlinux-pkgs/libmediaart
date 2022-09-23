#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmediaart
Version  : 1.9.6
Release  : 13
URL      : https://download.gnome.org/sources/libmediaart/1.9/libmediaart-1.9.6.tar.xz
Source0  : https://download.gnome.org/sources/libmediaart/1.9/libmediaart-1.9.6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libmediaart-data = %{version}-%{release}
Requires: libmediaart-lib = %{version}-%{release}
Requires: libmediaart-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gdk-pixbuf

%description
libmediaart
===========
Library tasked with managing, extracting and handling media art caches

%package data
Summary: data components for the libmediaart package.
Group: Data

%description data
data components for the libmediaart package.


%package dev
Summary: dev components for the libmediaart package.
Group: Development
Requires: libmediaart-lib = %{version}-%{release}
Requires: libmediaart-data = %{version}-%{release}
Provides: libmediaart-devel = %{version}-%{release}
Requires: libmediaart = %{version}-%{release}

%description dev
dev components for the libmediaart package.


%package lib
Summary: lib components for the libmediaart package.
Group: Libraries
Requires: libmediaart-data = %{version}-%{release}
Requires: libmediaart-license = %{version}-%{release}

%description lib
lib components for the libmediaart package.


%package license
Summary: license components for the libmediaart package.
Group: Default

%description license
license components for the libmediaart package.


%prep
%setup -q -n libmediaart-1.9.6
cd %{_builddir}/libmediaart-1.9.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1654116910
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libmediaart
cp %{_builddir}/libmediaart-1.9.6/COPYING %{buildroot}/usr/share/package-licenses/libmediaart/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/libmediaart-1.9.6/COPYING.LESSER %{buildroot}/usr/share/package-licenses/libmediaart/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/MediaArt-2.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/libmediaart-2.0.deps
/usr/share/vala/vapi/libmediaart-2.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libmediaart-2.0/libmediaart/cache.h
/usr/include/libmediaart-2.0/libmediaart/extract.h
/usr/include/libmediaart-2.0/libmediaart/extractgeneric.h
/usr/include/libmediaart-2.0/libmediaart/mediaart-macros.h
/usr/include/libmediaart-2.0/libmediaart/mediaart.h
/usr/lib64/libmediaart-2.0.so
/usr/lib64/pkgconfig/libmediaart-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmediaart-2.0.so.0
/usr/lib64/libmediaart-2.0.so.0.906.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmediaart/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libmediaart/4cc77b90af91e615a64ae04893fdffa7939db84c
