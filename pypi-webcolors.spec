#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D9266A6808FE067 (james@b-list.org)
#
Name     : pypi-webcolors
Version  : 1.12
Release  : 68
URL      : https://files.pythonhosted.org/packages/5f/f5/004dabd8f86abe0e770df4bcde8baf658709d3ebdd4d8fa835f6680012bb/webcolors-1.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/f5/004dabd8f86abe0e770df4bcde8baf658709d3ebdd4d8fa835f6680012bb/webcolors-1.12.tar.gz
Source1  : https://files.pythonhosted.org/packages/5f/f5/004dabd8f86abe0e770df4bcde8baf658709d3ebdd4d8fa835f6680012bb/webcolors-1.12.tar.gz.asc
Summary  : A library for working with color names and color values formats defined by HTML and CSS.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-webcolors-license = %{version}-%{release}
Requires: pypi-webcolors-python = %{version}-%{release}
Requires: pypi-webcolors-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://github.com/ubernostrum/webcolors/workflows/CI/badge.svg
:alt: CI status image
:target: https://github.com/ubernostrum/webcolors/actions?query=workflow%3ACI

%package license
Summary: license components for the pypi-webcolors package.
Group: Default

%description license
license components for the pypi-webcolors package.


%package python
Summary: python components for the pypi-webcolors package.
Group: Default
Requires: pypi-webcolors-python3 = %{version}-%{release}

%description python
python components for the pypi-webcolors package.


%package python3
Summary: python3 components for the pypi-webcolors package.
Group: Default
Requires: python3-core
Provides: pypi(webcolors)

%description python3
python3 components for the pypi-webcolors package.


%prep
%setup -q -n webcolors-1.12
cd %{_builddir}/webcolors-1.12
pushd ..
cp -a webcolors-1.12 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656362201
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-webcolors
cp %{_builddir}/webcolors-1.12/LICENSE %{buildroot}/usr/share/package-licenses/pypi-webcolors/40b7920b95636927d4a0f3b83a045aeec4016f0d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-webcolors/40b7920b95636927d4a0f3b83a045aeec4016f0d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
