#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2D9266A6808FE067 (james@b-list.org)
#
Name     : webcolors
Version  : 1.5
Release  : 10
URL      : https://pypi.python.org/packages/source/w/webcolors/webcolors-1.5.tar.gz
Source0  : https://pypi.python.org/packages/source/w/webcolors/webcolors-1.5.tar.gz
Source99 : https://pypi.python.org/packages/source/w/webcolors/webcolors-1.5.tar.gz.asc
Summary  : A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: webcolors-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
``webcolors`` is a simple Python module for working with HTML/CSS
color definitions.

%package python
Summary: python components for the webcolors package.
Group: Default

%description python
python components for the webcolors package.


%prep
%setup -q -n webcolors-1.5

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484583918
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484583918
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
