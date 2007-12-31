Summary:	openSUSE (build service) commander
Name:		osc
Version:	0.99
Release:	0.1
License:	GPL
Group:		Applications
URL:		https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/clientlib/python/osc/
# v=0.99; svn export https://forgesvn1.novell.com/svn/opensuse/trunk/buildservice/src/clientlib/python/osc osc-$v; tar czf osc-$v.tar.gz osc-$v
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	7bb8b2a25911bc1868a3c2cdf58da138
BuildRequires:	python-devel
Requires:	python-elementtree
Requires:	python-rpm
Requires:	python-urlgrabber
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Commandline client for the openSUSE build service.

See <http://en.opensuse.org/Build_Service/CLI>, as well as
<http://en.opensuse.org/Build_Service_Tutorial> for a general
introduction.

%prep
%setup -q

%build
CFLAGS="%{optflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--prefix=%{_prefix} \
	--root $RPM_BUILD_ROOT

ln -s osc-wrapper.py $RPM_BUILD_ROOT%{_bindir}/osc
install -d $RPM_BUILD_ROOT/var/lib/osc-plugins

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO NEWS
%attr(755,root,root) %{_bindir}/osc*
%dir %{py_sitescriptdir}/osc
%{py_sitescriptdir}/osc/*.py[co]
%dir /var/lib/osc-plugins
