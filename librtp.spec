Summary:	RTP/RTCP protocol library
Summary(pl.UTF-8):   Biblioteka obsługująca protokół RTP/RTCP
Name:		librtp
Version:	0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/librtp/%{name}-%{version}.tar.gz
# Source0-md5:	697d560425fbb1759d51390481e50491
URL:		http://librtp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2
BuildRequires:	libtool
Requires:	glib >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librtp is a library for handling RTP/RTCP packets. (See RFC 1889 and
1890 for more information about the protocol)

%description -l pl.UTF-8
librtp to biblioteka obsługująca pakiety RTP/RTCP. Więcej informacji o
protokole znajduje się w RFC 1889 i 1890.

%package devel
Summary:	Header files to develop applications using librtp
Summary(pl.UTF-8):   Pliki nagłówkowe do tworzenia aplikacji używających librtp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for the librtp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki librtp.

%package static
Summary:	Static librtp library
Summary(pl.UTF-8):   Statyczna biblioteka librtp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librtp library.

%description static -l pl.UTF-8
Statyczna biblioteka librtp.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -fr $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO NEWS AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/rtp

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
