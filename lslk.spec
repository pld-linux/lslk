Summary:	A lock file lister
Name:		lslk
Version:	1.27
Release:	2
Copyright:	Free
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source0:	ftp://vic.cc.purdue.edu/pub/tools/unix/lslk/%{name}_%{version}_W.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lslk is a lock file lister. Lslk attempts to list all of the locks on
the executing system's local files (i.e., on the active inodes).
Install lslk if you need a utility for listing file locks.

%prep
%setup -q -c -n lslk
tar xf lslk_%{version}.tar

%build
cd lslk_%{version}
./Configure -n linux
%{__make} DEBUG="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

cd lslk_%{version}

install lslk $RPM_BUILD_ROOT%{_sbindir}
install lslk.8 $RPM_BUILD_ROOT%{_mandir}/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# XXX should be mode 4755, but for now leave the setuid off
%attr(0755,root,root) %{_sbindir}/lslk
%{_mandir}/man8/*
