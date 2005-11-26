%include	/usr/lib/rpm/macros.php
%define		_class		Archive
%define		_subclass	Zip
%define		_status		beta
%define		_pearname	Archive_Zip

Summary:	%{_pearname} - Zip file management class
Summary(pl):	%{_pearname} - klasa do zarz±dzania archiwami Zip
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4aaf67077f36aca326ecee8160f78b7d
URL:		http://pear.php.net/package/Archive_Zip/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides handling of zip files in PHP.
It supports creating, listing, extracting and adding to zip files.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa pozwala na obs³ugê plików zip w PHP.
Wspiera tworzenia, wy¶wietlanie listy plików, wydobywanie oraz dodawanie
ich do archiwów zip.

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
