#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: eaa4f711da30
#
Name     : direwolf
Version  : 1.7
Release  : 25
URL      : https://github.com/wb2osz/direwolf/archive/1.7/direwolf-1.7.tar.gz
Source0  : https://github.com/wb2osz/direwolf/archive/1.7/direwolf-1.7.tar.gz
Summary  : Sound Card-based AX.25 TNC
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ GPL-3.0 ISC
Requires: direwolf-bin = %{version}-%{release}
Requires: direwolf-config = %{version}-%{release}
Requires: direwolf-data = %{version}-%{release}
Requires: direwolf-license = %{version}-%{release}
Requires: direwolf-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(avahi-core)
BuildRequires : pkgconfig(hamlib)
BuildRequires : pkgconfig(libgps)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(portaudio-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Dire Wolf is a modern software replacement for the old 1980's style
TNC built with special hardware.  Without any additional software, it
can perform as an APRS GPS Tracker, Digipeater, Internet Gateway
(IGate), APRStt gateway. It can also be used as a virtual TNC for
other applications such as APRSIS32, UI-View32, Xastir, APRS-TW, YAAC,
UISS, Linux AX25, SARTrack, Winlink Express, BPQ32, Outpost PM, and many
others.

%package bin
Summary: bin components for the direwolf package.
Group: Binaries
Requires: direwolf-data = %{version}-%{release}
Requires: direwolf-config = %{version}-%{release}
Requires: direwolf-license = %{version}-%{release}

%description bin
bin components for the direwolf package.


%package config
Summary: config components for the direwolf package.
Group: Default

%description config
config components for the direwolf package.


%package data
Summary: data components for the direwolf package.
Group: Data

%description data
data components for the direwolf package.


%package doc
Summary: doc components for the direwolf package.
Group: Documentation
Requires: direwolf-man = %{version}-%{release}

%description doc
doc components for the direwolf package.


%package license
Summary: license components for the direwolf package.
Group: Default

%description license
license components for the direwolf package.


%package man
Summary: man components for the direwolf package.
Group: Default

%description man
man components for the direwolf package.


%prep
%setup -q -n direwolf-1.7
cd %{_builddir}/direwolf-1.7
pushd ..
cp -a direwolf-1.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723578329
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../../buildavx2/clr-build-avx2;
make test || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723578329
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/direwolf
cp %{_builddir}/direwolf-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/direwolf/0f0e2ead1017d225cc9c0c356708088dfa21825d || :
cp %{_builddir}/direwolf-%{version}/external/hidapi/LICENSE-bsd.txt %{buildroot}/usr/share/package-licenses/direwolf/7dde42b4c6fdafae722d8d07556b6d9dba4d2963 || :
cp %{_builddir}/direwolf-%{version}/external/hidapi/LICENSE-gpl3.txt %{buildroot}/usr/share/package-licenses/direwolf/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/direwolf-%{version}/external/hidapi/LICENSE-orig.txt %{buildroot}/usr/share/package-licenses/direwolf/66047dbcf3fd689c99472266f5ad141c53d6f2c6 || :
cp %{_builddir}/direwolf-%{version}/external/regex/COPYING %{buildroot}/usr/share/package-licenses/direwolf/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/lib
mv %{buildroot}/etc/udev %{buildroot}/usr/lib/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/aclients
/V3/usr/bin/appserver
/V3/usr/bin/atest
/V3/usr/bin/cm108
/V3/usr/bin/decode_aprs
/V3/usr/bin/direwolf
/V3/usr/bin/gen_packets
/V3/usr/bin/kissutil
/V3/usr/bin/ll2utm
/V3/usr/bin/log2gpx
/V3/usr/bin/text2tt
/V3/usr/bin/tnctest
/V3/usr/bin/tt2text
/V3/usr/bin/ttcalc
/V3/usr/bin/utm2ll
/usr/bin/aclients
/usr/bin/appserver
/usr/bin/atest
/usr/bin/cm108
/usr/bin/decode_aprs
/usr/bin/direwolf
/usr/bin/dwespeak.sh
/usr/bin/gen_packets
/usr/bin/kissutil
/usr/bin/ll2utm
/usr/bin/log2gpx
/usr/bin/telem-balloon.pl
/usr/bin/telem-bits.pl
/usr/bin/telem-data.pl
/usr/bin/telem-data91.pl
/usr/bin/telem-eqns.pl
/usr/bin/telem-parm.pl
/usr/bin/telem-seq.sh
/usr/bin/telem-unit.pl
/usr/bin/telem-volts.py
/usr/bin/text2tt
/usr/bin/tnctest
/usr/bin/tt2text
/usr/bin/ttcalc
/usr/bin/utm2ll

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/99-direwolf-cmedia.rules

%files data
%defattr(-,root,root,-)
/usr/share/applications/direwolf.desktop
/usr/share/direwolf/symbols-new.txt
/usr/share/direwolf/symbolsX.txt
/usr/share/direwolf/tocalls.txt
/usr/share/pixmaps/direwolf_icon.png

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/direwolf/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/direwolf/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
/usr/share/package-licenses/direwolf/0f0e2ead1017d225cc9c0c356708088dfa21825d
/usr/share/package-licenses/direwolf/66047dbcf3fd689c99472266f5ad141c53d6f2c6
/usr/share/package-licenses/direwolf/7dde42b4c6fdafae722d8d07556b6d9dba4d2963
/usr/share/package-licenses/direwolf/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/aclients.1
/usr/share/man/man1/atest.1
/usr/share/man/man1/decode_aprs.1
/usr/share/man/man1/direwolf.1
/usr/share/man/man1/gen_packets.1
/usr/share/man/man1/kissutil.1
/usr/share/man/man1/ll2utm.1
/usr/share/man/man1/log2gpx.1
/usr/share/man/man1/text2tt.1
/usr/share/man/man1/tt2text.1
/usr/share/man/man1/utm2ll.1
