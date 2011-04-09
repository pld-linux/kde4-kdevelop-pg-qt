%define		_state		stable
%define		kdever		4.6.2
%define		qtver		4.7.2
%define		orgname		kdevelop-pg-qt

Summary:	The parser-generator from KDevplatform
Name:		kde4-kdevelop-pg-qt
Version:	0.9.5
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{orgname}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	4818af0deea47d583adff7c134d62e08
URL:		http://www.kdevelop.org/
BuildRequires:	automoc4
BuildRequires:	bison
BuildRequires:	cmake >= 2.8.0
BuildRequires:	flex
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDevelop-PG-Qt is the parser-generator from KDevplatform. It is used
for some KDevelop-languagesupport-plugins (Ruby, PHP, Java...).

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdev-pg-qt
%{_includedir}/%{orgname}
%{_datadir}/apps/cmake/modules/FindKDevelop-PG-Qt.cmake
