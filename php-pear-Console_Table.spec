%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	Table
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - makes it easy to build console style tables
Summary(pl):	%{_pearname} - proste tworzenie tabel konsolowych
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	758e7e57b687464c831cba9cf038bc8b
URL:		http://pear.php.net/package/Console_Table/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides methods such as addRow(), insertRow(), addCol() etc to build
Console tables. Can be with or without headers, and has various
configurable options.

In PEAR status of this package is: %{_status}.

%description -l pl
Dostarcza metod, takich jak addRow(), insertRow(), addCol(), itp. do
tworzenia tabel konsolowych. Mog± byæ robione z i bez nag³ówków.
Posiada wiele opcji konfigurowalnych.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
