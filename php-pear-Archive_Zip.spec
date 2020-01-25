%define		_class		Archive
%define		_subclass	Zip
%define		_status		beta
%define		_pearname	Archive_Zip

Summary:	%{_pearname} - Zip file management class
Summary(pl.UTF-8):	%{_pearname} - klasa do zarządzania archiwami Zip
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5d5cb390b8c2aa19af36db50d95ce801
URL:		http://pear.php.net/package/Archive_Zip/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides handling of zip files in PHP. It supports
creating, listing, extracting and adding to zip files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa pozwala na obsługę plików zip w PHP. Obsługuje tworzenie,
wyświetlanie listy plików, wydobywanie oraz dodawanie ich do archiwów
zip.

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
%{php_pear_dir}/Archive/Zip.php
