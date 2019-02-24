%define		status		stable
%define		pearname	Console_Table
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - makes it easy to build console style tables
Summary(pl.UTF-8):	%{pearname} - proste tworzenie tabel konsolowych
Name:		php-pear-%{pearname}
Version:	1.3.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	6b84a527b3a1cf6be26c66863bae2ace
URL:		http://pear.php.net/package/Console_Table/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear
Suggests:	php-pear-Console_Color2
Obsoletes:	php-pear-Console_Table-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear	Console/Color2.*

%description
Provides methods such as addRow(), insertRow(), addCol() etc to build
Console tables. Can be with or without headers, and has various
configurable options.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Dostarcza metod, takich jak addRow(), insertRow(), addCol(), itp. do
tworzenia tabel konsolowych. Mogą być robione z i bez nagłówków.
Posiada wiele opcji konfigurowalnych.

Ta klasa ma w PEAR status: %{status}.

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
%{php_pear_dir}/Console/Table.php
