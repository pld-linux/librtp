
Summary:	RTP/RTCP protocol library
Name:		librtp
Version:	0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://unc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://librtp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	glib >= 1.2
BuildRequires:	glib-devel >= 1.2

%description
librtp is a library for handling RTP/RTCP packets. (See RFC 1889 and
1890 for more information about the protocol)

%package devel
Group:		Development/Libraries
Summary:	Header files to develop applications using librtp.
Requires:	%{name} = %{version}

%description devel
Header files for the librtp library.

%package static
Group:		Development/Libraries
Summary:	Static file for librtp.
Requires:	%{name}-devel = %{version}

%description static
Static file for librtp.

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

%files
%defattr(644,root,root,755)
%doc README TODO NEWS AUTHORS COPYING ChangeLog
%{_libdir}/librtp*.so*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_includedir}/rtp/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
