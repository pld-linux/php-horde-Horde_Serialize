%define		status		stable
%define		pearname	Horde_Serialize
Summary:	%{pearname} - Data Encapulation API
Name:		php-horde-Horde_Serialize
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	f306bf4571023900486aa62ea824a261
URL:		https://github.com/horde/horde/tree/master/framework/Serialize/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php(bz2)
Suggests:	php(json)
Suggests:	php(lzf)
Suggests:	php(wddx)
Suggests:	php(zlib)
Suggests:	php-horde-Horde_Imap_Client
Suggests:	php-horde-Horde_Mime
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Imap/Client.*) pear(Horde/Mime.*)

%description
The Horde_Serialize library provides various methods of encapsulating
data.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/Horde_Serialize/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Serialize.php
%{php_pear_dir}/Horde/Serialize
