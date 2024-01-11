%{!?_licensedir:%global license %%doc}

%global srcname yubico

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{srcname}
Version:        1.3.2
Release:        9.1%{?dist}
Summary:        Pure-python library for interacting with Yubikeys

License:        BSD
URL:            https://github.com/Yubico/%{name}
Source0:        https://github.com/Yubico/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:         python-yubico-py3.patch

BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
BuildRequires:  python2-pyusb
%endif # with python2

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-pyusb

%description
Pure-python library for interacting with Yubikeys

%if %{with python2}
%package -n python2-%{srcname}
Summary:        Pure-python library for interacting with Yubikeys
Requires:       pyusb
Obsoletes:      python-yubico < %{version}-%{release}

%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Pure-python library for interacting with Yubikeys. For Python 2.
%endif # with python2

%package -n python3-%{srcname}
Summary:        Pure-python library for interacting with Yubikeys
Requires:       python3-pyusb

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Pure-python library for interacting with Yubikeys. For Python 3.


%prep
%autosetup -n %{name}-%{name}-%{version} -p1


%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build


%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install


%check
%if %{with python2}
nosetests-%{python2_version} -e test_challenge_response -e test_serial -e test_status
%endif # with python2
nosetests-%{python3_version} -e test_challenge_response -e test_serial -e test_status

%if %{with python2}
%files -n python2-%{srcname}
%license COPYING
%doc NEWS README
%{python2_sitelib}/*
%endif # with python2

%files -n python3-%{srcname}
%license COPYING
%doc NEWS README
%{python3_sitelib}/*


%changelog
* Thu Jun 16 2022 Florence Blanc-Renaud <frenaud@redhat.com> - 1.3.2-9.1
- Rebuilt to fix NVR issue (#2097803)

* Tue Jun 19 2018 Charalampos Stratakis <cstratak@redhat.com> - 1.3.2-9
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Nathaniel McCallum <npmccallum@redhat.com> - 1.3.2-7
- Backport an upstream python3 fix (#1484862)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 11 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.3.2-2
- Add missing provide for python-yubico
- Add missing obsoletes for python-yubico

* Tue May 10 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.3.2-1
- Cleanup obsolete conditions (like RHEL 6)
- Update to v1.3.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Will Thompson <will@willthompson.co.uk> - 1.2.3-5
- Add python3-pyusb dependency to python3 subpackage (#1278210)

* Mon Jan 11 2016 Ville Skyttä <ville.skytta@iki.fi>
- Ship COPYING as %%license where applicable

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Jul 20 2015 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-3
- Add Python 3 subpackage (#1244237)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.3-1
- Upstream 1.2.3
- Require pyusb during building when running tests

* Mon Jun 23 2014 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.1-3
- Enable build on EL6.

* Sat Jun 21 2014 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.1-2
- Run upstream tests during build.

* Thu Jun 19 2014 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.1-1
- Initial release.
