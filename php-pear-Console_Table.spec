%define		_class		Console
%define		_subclass	Table
%define		_status		stable
%define		_pearname	Console_Table
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - makes it easy to build console style tables
Summary(pl.UTF-8):	%{_pearname} - proste tworzenie tabel konsolowych
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a491b94bf40c3fed90feac6d7807ba0b
URL:		http://pear.php.net/package/Console_Table/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear
Suggests:	php-pear-Console_Color
Obsoletes:	php-pear-Console_Table-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define	_noautoreq_pear Console/Color.php

%description
Provides methods such as addRow(), insertRow(), addCol() etc to build
Console tables. Can be with or without headers, and has various
configurable options.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza metod, takich jak addRow(), insertRow(), addCol(), itp. do
tworzenia tabel konsolowych. Mogą być robione z i bez nagłówków.
Posiada wiele opcji konfigurowalnych.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/Console/*.php
