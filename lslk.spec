Summary:	A lock file lister
Summary(pl.UTF-8):   Program wypisujący pliki blokujące
Name:		lslk
Version:	1.29
Release:	4
License:	Free
Group:		Development/Debuggers
Source0:	ftp://vic.cc.purdue.edu/pub/tools/unix/lslk/%{name}_%{version}_W.tar.gz
# Source0-md5:	cbd17b18bb7ad435c604aa7dc2026c47
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lslk is a lock file lister. Lslk attempts to list all of the locks on
the executing system's local files (i.e., on the active inodes).
Install lslk if you need a utility for listing file locks.

%description -l pl.UTF-8
lslk to program wypisujący pliki blokujące. Próbuje wypisać wszystkie
blokady na lokalnych plikach (czyli aktywnych inodach).

%prep
%setup -q -c -n lslk
tar xf lslk_%{version}.tar

# force linux/proc dialect even if /proc is not mounted on builder
sed -e 's@test -r /proc/locks@true@' lslk_%{version}/Configure > c.tmp
mv -f c.tmp lslk_%{version}/Configure
chmod +x lslk_%{version}/Configure

%build
cd lslk_%{version}
./Configure -n linux
%{__make} \
	DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

cd lslk_%{version}

install lslk $RPM_BUILD_ROOT%{_sbindir}
install lslk.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# XXX should be mode 4755, but for now leave the setuid off
%attr(755,root,root) %{_sbindir}/lslk
%{_mandir}/man8/*
