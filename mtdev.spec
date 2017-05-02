#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mtdev
Version  : 1.1.5
Release  : 9
URL      : http://bitmath.org/code/mtdev/mtdev-1.1.5.tar.gz
Source0  : http://bitmath.org/code/mtdev/mtdev-1.1.5.tar.gz
Summary  : Multitouch Protocol Translation Library
Group    : Development/Tools
License  : MIT
Requires: mtdev-bin
Requires: mtdev-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
mtdev - Multitouch Protocol Translation Library (MIT license)
The mtdev library transforms all variants of kernel MT events to the
slotted type B protocol. The events put into mtdev may be from any MT
device, specifically type A without contact tracking, type A with
contact tracking, or type B with contact tracking. See the kernel
documentation for further details.

%package bin
Summary: bin components for the mtdev package.
Group: Binaries

%description bin
bin components for the mtdev package.


%package dev
Summary: dev components for the mtdev package.
Group: Development
Requires: mtdev-lib
Requires: mtdev-bin
Provides: mtdev-devel

%description dev
dev components for the mtdev package.


%package dev32
Summary: dev32 components for the mtdev package.
Group: Default
Requires: mtdev-lib32
Requires: mtdev-bin
Requires: mtdev-dev

%description dev32
dev32 components for the mtdev package.


%package lib
Summary: lib components for the mtdev package.
Group: Libraries

%description lib
lib components for the mtdev package.


%package lib32
Summary: lib32 components for the mtdev package.
Group: Default

%description lib32
lib32 components for the mtdev package.


%prep
%setup -q -n mtdev-1.1.5
pushd ..
cp -a mtdev-1.1.5 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484342384
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mtdev-test

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libmtdev.so
/usr/lib64/pkgconfig/mtdev.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libmtdev.so
/usr/lib32/pkgconfig/32mtdev.pc
/usr/lib32/pkgconfig/mtdev.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmtdev.so.1
/usr/lib64/libmtdev.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libmtdev.so.1
/usr/lib32/libmtdev.so.1.0.0
