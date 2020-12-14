#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D9266A6808FE067 (james@b-list.org)
#
Name     : webcolors
Version  : 1.11.1
Release  : 52
URL      : https://files.pythonhosted.org/packages/a7/df/b97bf02a97bbd5ed874fec7c5418bf0dd51e8d042ac46bbf2bf5983e89fd/webcolors-1.11.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a7/df/b97bf02a97bbd5ed874fec7c5418bf0dd51e8d042ac46bbf2bf5983e89fd/webcolors-1.11.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/a7/df/b97bf02a97bbd5ed874fec7c5418bf0dd51e8d042ac46bbf2bf5983e89fd/webcolors-1.11.1.tar.gz.asc
Summary  : A library for working with color names and color values formats defined by HTML and CSS.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: webcolors-license = %{version}-%{release}
Requires: webcolors-python = %{version}-%{release}
Requires: webcolors-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://travis-ci.org/ubernostrum/webcolors.svg?branch=master
:target: https://travis-ci.org/ubernostrum/webcolors

%package license
Summary: license components for the webcolors package.
Group: Default

%description license
license components for the webcolors package.


%package python
Summary: python components for the webcolors package.
Group: Default
Requires: webcolors-python3 = %{version}-%{release}

%description python
python components for the webcolors package.


%package python3
Summary: python3 components for the webcolors package.
Group: Default
Requires: python3-core
Provides: pypi(webcolors)

%description python3
python3 components for the webcolors package.


%prep
%setup -q -n webcolors-1.11.1
cd %{_builddir}/webcolors-1.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603407486
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/webcolors
cp %{_builddir}/webcolors-1.11.1/LICENSE %{buildroot}/usr/share/package-licenses/webcolors/a9f86b6cbdd1bf9bacc6621af2fd3a0af5a5d194
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/webcolors/a9f86b6cbdd1bf9bacc6621af2fd3a0af5a5d194

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
