Name:          liblc3
Version:       1.1.3
Release:       1%{?dist}
Summary:       Low Complexity Communication Codec (LC3)

License:       Apache-2.0
URL:           https://github.com/google/liblc3
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:        0001-Revert-build-fix-rpath-issue.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: python3-devel

%description
The Low Complexity Communication Codec (LC3) is used by
Bluetooth as the codec for LE Audio. It enables high
quality audio over the low bandwidth connections provided
by Bluetooth LE.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package -n python3-lc3
Summary: Python3 bindings for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description -n python3-lc3
Python3 bindings for %{name}.

%package utils
Summary: Utility package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Uitlities for command line use of and testing
the %{name} library.

%prep
%autosetup -p1

%build
%meson -Dtools=true -Dpython=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%{_libdir}/liblc3.so.1{,.*}

%files devel
%{_includedir}/lc3*
%{_libdir}/pkgconfig/lc3.pc
%{_libdir}/liblc3.so

%files -n python3-lc3
%pycached %{python3_sitelib}/lc3.py

%files utils
%{_bindir}/dlc3
%{_bindir}/elc3

%changelog
* Sun Nov 09 2025 Neal Gompa <ngompa@centosproject.org> - 1.1.3-1
- Rebase to 1.1.3
  Resolves: RHEL-127169

* Tue Jun 17 2025 Tomas Pelka <tpelka@redhat.com> - 1.0.4-7
- Bump release for CRB inclusion
  Resolves: RHEL-96893

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 1.0.4-6
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 1.0.4-5
- Bump release for June 2024 mass rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 13 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.4-2
- Review fixes

* Fri Aug 04 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- Review updates
- Split utils out to subpackage

* Thu Jun 22 2023 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.3-1
- Initial package
