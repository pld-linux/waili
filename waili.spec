Summary:	WAILI - a wavelet transform library
Summary(pl.UTF-8):	WAILI - biblioteka transformaty falkowej
Name:		waili
Version:	19990723
Release:	1
License:	GPL v2+
Group:		Libraries
# Source0Download: https://nalag.cs.kuleuven.be/research/software/wavelets/Download.html
Source0:	https://nalag.cs.kuleuven.be/research/software/wavelets/%{name}-gpl-%{version}.tar.gz
# Source0-md5:	0bdbb8f6e1e44a575a5aebd7bca7fdcd
# Debian patches
Patch0:		%{name}-various_code.patch
Patch1:		%{name}-rangecheck.patch
Patch2:		%{name}-makefiles.patch
Patch3:		%{name}-gtk.patch
Patch4:		%{name}-doc-files.patch
Patch5:		%{name}-dpkg-buildflags.patch
Patch6:		%{name}-reproducible_build.patch
# PLD
Patch10:	%{name}-libtool_tag_cxx.patch
Patch11:	%{name}-optflags.patch
Patch12:	%{name}-libdir.patch
URL:		https://nalag.cs.kuleuven.be/research/software/wavelets/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WAILI is a wavelet transform library. It includes some basic image
processing operations based on the use of wavelets and forms the
backbone of more complex image processing operations.

%description -l pl.UTF-8
WAILI to biblioteka transformaty falkowej (wavelet transform). Zawiera
trochę podstawowych operacji przetwarzania obrazu opartych na użyciu
falek i stanowi szkielet dla bardziej złożonych operacji przetwarzania
obrazu.

%package devel
Summary:	Header files for WAILI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki WAILI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libstdc++-devel
Requires:	libtiff-devel

%description devel
Header files for WAILI library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki WAILI.

%package static
Summary:	Static WAILI library
Summary(pl.UTF-8):	Statyczna biblioteka WAILI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WAILI library.

%description static -l pl.UTF-8
Statyczna biblioteka WAILI.

%prep
%setup -q -n %{name}-gpl-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1

%build
%{__make} -C config \
	CXX="%{__cxx}" \
	LIBDIR=%{_libdir} \
	OPTCPPFLAGS="%{rpmcppflags}" \
	OPTCXXFLAGS="%{rpmcxxflags}" \
	OPTLDFLAGS="%{rpmldflags}"
%{__make} \
	CXX="%{__cxx}" \
	LIBDIR=%{_libdir} \
	OPTCPPFLAGS="%{rpmcppflags}" \
	OPTCXXFLAGS="%{rpmcxxflags}" \
	OPTLDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwaili.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwaili.so.0

%files devel
%defattr(644,root,root,755)
%doc man/Manual.ps
%attr(755,root,root) %{_libdir}/libwaili.so
%{_libdir}/libwaili.la
%{_includedir}/waili

%files static
%defattr(644,root,root,755)
%{_libdir}/libwaili.a
