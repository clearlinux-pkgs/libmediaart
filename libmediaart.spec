#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmediaart
Version  : 1.9.4
Release  : 4
URL      : https://download.gnome.org/sources/libmediaart/1.9/libmediaart-1.9.4.tar.xz
Source0  : https://download.gnome.org/sources/libmediaart/1.9/libmediaart-1.9.4.tar.xz
Summary  : libmediaart - Media art extraction and cache management library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libmediaart-lib
Requires: libmediaart-doc
Requires: libmediaart-data
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : gdk-pixbuf
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : python3

%description


%package data
Summary: data components for the libmediaart package.
Group: Data

%description data
data components for the libmediaart package.


%package dev
Summary: dev components for the libmediaart package.
Group: Development
Requires: libmediaart-lib
Requires: libmediaart-data
Provides: libmediaart-devel

%description dev
dev components for the libmediaart package.


%package doc
Summary: doc components for the libmediaart package.
Group: Documentation

%description doc
doc components for the libmediaart package.


%package lib
Summary: lib components for the libmediaart package.
Group: Libraries
Requires: libmediaart-data

%description lib
lib components for the libmediaart package.


%prep
%setup -q -n libmediaart-1.9.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511464418
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1511464418
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/MediaArt-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libmediaart-2.0/libmediaart/cache.h
/usr/include/libmediaart-2.0/libmediaart/extract.h
/usr/include/libmediaart-2.0/libmediaart/extractgeneric.h
/usr/include/libmediaart-2.0/libmediaart/mediaart-macros.h
/usr/include/libmediaart-2.0/libmediaart/mediaart.h
/usr/lib64/libmediaart-2.0.so
/usr/lib64/pkgconfig/libmediaart-2.0.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libmediaart/annotation-glossary.html
/usr/share/gtk-doc/html/libmediaart/ch02.html
/usr/share/gtk-doc/html/libmediaart/home.png
/usr/share/gtk-doc/html/libmediaart/index.html
/usr/share/gtk-doc/html/libmediaart/left-insensitive.png
/usr/share/gtk-doc/html/libmediaart/left.png
/usr/share/gtk-doc/html/libmediaart/libmediaart-Cache.html
/usr/share/gtk-doc/html/libmediaart/libmediaart-MediaArtProcess.html
/usr/share/gtk-doc/html/libmediaart/libmediaart-Plugins.html
/usr/share/gtk-doc/html/libmediaart/libmediaart-reference.html
/usr/share/gtk-doc/html/libmediaart/libmediaart.devhelp2
/usr/share/gtk-doc/html/libmediaart/overview-compiling.html
/usr/share/gtk-doc/html/libmediaart/overview.html
/usr/share/gtk-doc/html/libmediaart/right-insensitive.png
/usr/share/gtk-doc/html/libmediaart/right.png
/usr/share/gtk-doc/html/libmediaart/style.css
/usr/share/gtk-doc/html/libmediaart/up-insensitive.png
/usr/share/gtk-doc/html/libmediaart/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmediaart-2.0.so.0
/usr/lib64/libmediaart-2.0.so.0.904.0
