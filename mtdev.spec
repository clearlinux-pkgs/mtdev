#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mtdev
Version  : 1.1.5
Release  : 3
URL      : http://bitmath.org/code/mtdev/mtdev-1.1.5.tar.gz
Source0  : http://bitmath.org/code/mtdev/mtdev-1.1.5.tar.gz
Summary  : Multitouch Protocol Translation Library
Group    : Development/Tools
License  : MIT
Requires: mtdev-bin
Requires: mtdev-lib

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

%description dev
dev components for the mtdev package.


%package lib
Summary: lib components for the mtdev package.
Group: Libraries

%description lib
lib components for the mtdev package.


%prep
%setup -q -n mtdev-1.1.5

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mtdev-test

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
