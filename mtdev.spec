#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mtdev
Version  : 1.1.6
Release  : 13
URL      : https://bitmath.org/code/mtdev/mtdev-1.1.6.tar.gz
Source0  : https://bitmath.org/code/mtdev/mtdev-1.1.6.tar.gz
Summary  : Multitouch Protocol Translation Library
Group    : Development/Tools
License  : MIT
Requires: mtdev-bin = %{version}-%{release}
Requires: mtdev-lib = %{version}-%{release}
Requires: mtdev-license = %{version}-%{release}
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
Requires: mtdev-license = %{version}-%{release}

%description bin
bin components for the mtdev package.


%package dev
Summary: dev components for the mtdev package.
Group: Development
Requires: mtdev-lib = %{version}-%{release}
Requires: mtdev-bin = %{version}-%{release}
Provides: mtdev-devel = %{version}-%{release}
Requires: mtdev = %{version}-%{release}

%description dev
dev components for the mtdev package.


%package dev32
Summary: dev32 components for the mtdev package.
Group: Default
Requires: mtdev-lib32 = %{version}-%{release}
Requires: mtdev-bin = %{version}-%{release}
Requires: mtdev-dev = %{version}-%{release}

%description dev32
dev32 components for the mtdev package.


%package lib
Summary: lib components for the mtdev package.
Group: Libraries
Requires: mtdev-license = %{version}-%{release}

%description lib
lib components for the mtdev package.


%package lib32
Summary: lib32 components for the mtdev package.
Group: Default
Requires: mtdev-license = %{version}-%{release}

%description lib32
lib32 components for the mtdev package.


%package license
Summary: license components for the mtdev package.
Group: Default

%description license
license components for the mtdev package.


%prep
%setup -q -n mtdev-1.1.6
cd %{_builddir}/mtdev-1.1.6
pushd ..
cp -a mtdev-1.1.6 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583958023
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1583958023
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mtdev
cp %{_builddir}/mtdev-1.1.6/COPYING %{buildroot}/usr/share/package-licenses/mtdev/1870c2b9c61ff1cbd01583f181e6afa27bcce198
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
/usr/include/mtdev-mapping.h
/usr/include/mtdev-plumbing.h
/usr/include/mtdev.h
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mtdev/1870c2b9c61ff1cbd01583f181e6afa27bcce198
