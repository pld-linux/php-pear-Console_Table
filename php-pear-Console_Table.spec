%include	/usr/lib/rpm/macros.php
%define		_class		Console
%define		_subclass	Table
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - makes it easy to build console style tables
Summary(pl):	%{_pearname} - proste tworzenie tabel konsolowych
Name:		php-pear-%{_pearname}
Version:	0.8
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides methods such as addRow(), insertRow(), addCol() etc to build
Console tables. Can be with or without headers, and has various
configurable options.

%description -l pl
Dostarcza metod, takich jak addRow(), insertRow(), addCol(), itp. do
tworzenia tabel konsolowych. Mog� by� robione z i bez nag��wk�w.
Posiada wiele opcji konfigurowalnych.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
