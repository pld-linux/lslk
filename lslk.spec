Summary: A lock file lister.
Name: lslk
Version: 1.19
Release: 5
Copyright: Free
Group: Development/Debuggers
Source: ftp://vic.cc.purdue.edu/pub/tools/unix/lslk/lslk_%{version}_W.tar.gz
Prefix: %{_prefix}
Buildroot: /var/tmp/%{name}-root

%description
Lslk is a lock file lister.  Lslk attempts to list all of the locks on
the executing system's local files (i.e., on the active inodes).

Install lslk if you need a utility for listing file locks.

%prep
%setup -q -c -n lslk
tar xf lslk_%{version}.tar
[ -d lslk_%{version} ] && cd lslk_%{version}

%build
rm -rf $RPM_BUILD_ROOT
[ -d lslk_%{version} ] && cd lslk_%{version}
./Configure -n linux
make CFGF=-DLINUXV=21131

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/{sbin,man/man8}

[ -d lslk_%{version} ] && cd lslk_%{version}
install -s lslk ${RPM_BUILD_ROOT}%{_prefix}/sbin
install lslk.8 ${RPM_BUILD_ROOT}%{_prefix}/man/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# XXX should be mode 4755, but for now leave the setuid off
%attr(0755,root,kmem) %{_prefix}/sbin/lslk
%{_prefix}/man/man8/lslk.8
