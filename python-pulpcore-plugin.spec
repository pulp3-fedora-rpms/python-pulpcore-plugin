# Created by pyp2rpm-3.3.2
%global pypi_name pulpcore-plugin

Name:           python-%{pypi_name}
Version:        0.1.0b21
Release:        1%{?dist}
Summary:        Pulp Plugin API

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
**Pulp Plugin API**The Pulp Plugin API is an essential part of the Pulp Project
3.0+ < which provides a set of base classes that can be implemented in plugins
to manage content in a way that is consistent across plugins, while still
allowing plugin writers the freedom to define their workflows as they deem
necessary.The Pulp Plugin API allows plugin writers: - to easily define your
content...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(aiofiles)
Requires:       python3dist(aiohttp)
Requires:       python3dist(backoff)
Requires:       python3dist(pulpcore) >= 3.0.0b22
%description -n python3-%{pypi_name}
**Pulp Plugin API**The Pulp Plugin API is an essential part of the Pulp Project
3.0+ < which provides a set of base classes that can be implemented in plugins
to manage content in a way that is consistent across plugins, while still
allowing plugin writers the freedom to define their workflows as they deem
necessary.The Pulp Plugin API allows plugin writers: - to easily define your
content...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
# These files get copied over during the build process from pulpcore
%exclude %{python3_sitelib}/pulpcore/*.py*
%exclude %{python3_sitelib}/pulpcore/__pycache__/*.py*
%{python3_sitelib}/pulpcore/plugin
%{python3_sitelib}/pulpcore_plugin-%{version}-py?.?.egg-info

%changelog
* Tue Mar 26 2019 Mike DePaulo <mikedep333@redhat.com> - 0.1.0b21-1
- Initial package.
