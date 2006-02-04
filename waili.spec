Summary:	WAILI - a wavelet transform library
Summary(pl):	WAILI - biblioteka transformaty falkowej
Name:		waili
Version:	19990723
Release:	1
License:	GPL
Group:		Libraries
# Source0Download: http://www.cs.kuleuven.ac.be/~wavelets/Download.html
Source0:	http://www.cs.kuleuven.ac.be/~wavelets/%{name}-gpl-%{version}.tar.gz
# Source0-md5:	0bdbb8f6e1e44a575a5aebd7bca7fdcd
Patch0:		%{name}-debian.patch
URL:		http://www.cs.kuleuven.ac.be/~wavelets/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WAILI is a wavelet transform library. It includes some basic image
processing operations based on the use of wavelets and forms the
backbone of more complex image processing operations.

%description -l pl
WAILI to biblioteka transformaty falkowej (wavelet transform). Zawiera
trochê podstawowych operacji przetwarzania obrazu opartych na u¿yciu
falek i stanowi szkielet dla bardziej z³o¿onych operacji przetwarzania
obrazu.

%package devel
Summary:	Header files for WAILI library
Summary(pl):	Pliki nag³ówkowe biblioteki WAILI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libstdc++-devel
Requires:	libtiff-devel

%description devel
Header files for WAILI library.

%description devel -l pl
Pliki nag³ówkowe biblioteki WAILI.

%package static
Summary:	Static WAILI library
Summary(pl):	Statyczna biblioteka WAILI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WAILI library.

%description static -l pl
Statyczna biblioteka WAILI.

%prep
%setup -q -n %{name}-gpl-%{version}
%patch0 -p1

mv -f debian/changelog debian/changelog.Debian

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc debian/*
%attr(755,root,root) %{_libdir}/libwaili.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc man/Manual.ps
%attr(755,root,root) %{_libdir}/libwaili.so
%{_libdir}/libwaili.la
%{_includedir}/waili

%files static
%defattr(644,root,root,755)
%{_libdir}/libwaili.a
