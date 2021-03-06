# remirepo spec file for php-oojs-oojs-ui, from:
#
# Fedora spec file for php-oojs-oojs-ui
#
# License: MIT
# http://opensource.org/licenses/MIT
#
%global git_tag_rev 847c492f2ae8228a4b9ae866dc21212c60813820

Name:		php-oojs-oojs-ui
Version:	0.11.6
Release:	1%{?dist}
Summary:	Object-Oriented JavaScript – User Interface
Group:		Development/Libraries

License:	MIT
URL:		http://www.mediawiki.org/wiki/OOjs_UI
Source0:	http://git.wikimedia.org/zip/?r=oojs/ui.git&format=xz&h=%{git_tag_rev}#/%{name}-%{version}.tar.xz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Buildarch:	noarch

BuildRequires:  php-phpunit-PHPUnit
BuildRequires:  php-theseer-autoload

Requires:	php(language) >= 5.3.3
Requires:	php-json
Requires:	php-pcre
Requires:	php-spl

Provides:	php-composer(oojs/oojs-ui) = %{version}

%description
OOjs UI (Object-Oriented JavaScript – User Interface) is a library that allows
developers to rapidly create front-end web applications that operate
consistently across a multitude of browsers.


%prep
%setup -qc %{name}-%{version}


%build
phpab --output php/autoload.php php


%install
rm -rf %{buildroot}
mkdir -pm 0755 %{buildroot}%{_datadir}/php/OOUI
cp -rp php/* %{buildroot}%{_datadir}/php/OOUI


%check
phpunit -v --bootstrap php/autoload.php


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license LICENSE-MIT
%doc AUTHORS.txt composer.json History.md README.md
%{_datadir}/php/OOUI


%changelog
* Fri Jun 26 2015 Remi Collet <remi@remirepo.net> - 0.11.6-1
- backport for remirepo

* Thu Jun 25 2015 Michael Cronenworth <mike@cchtml.com> - 0.11.6-1
- Initial package

