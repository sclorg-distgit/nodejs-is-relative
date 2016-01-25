%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}
%global npm_name is-relative

Summary:       Returns true if the path appears to be relative.
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.2.1
Release:       2%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/is-relative
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Returns true if the path appears to be relative.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 0.2.1-2
- Enable scl macros

* Tue Nov 24 2015 Troy Dawson <tdawson@redhat.com> - 0.2.1-1
- Initial package
