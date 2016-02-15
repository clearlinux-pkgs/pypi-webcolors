#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : webcolors
Version  : 1.5
Release  : 3
URL      : https://pypi.python.org/packages/source/w/webcolors/webcolors-1.5.tar.gz
Source0  : https://pypi.python.org/packages/source/w/webcolors/webcolors-1.5.tar.gz
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
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
