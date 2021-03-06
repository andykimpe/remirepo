# Fedora spec file for php-Raven, from:
#
# Fedora spec file for php-Raven
#
# Copyright (c) 2013-2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#
%if 0%{?rhel} == 5
%global with_cacert 0
%else
%global with_cacert 1
%endif

%global github_owner    getsentry
%global github_name     raven-php
%global github_version  0.12.0
%global github_commit   bd247ca2a8fd9ccfb99b60285c9b31286384a92b

%global lib_name        Raven

# "php": ">=5.2.4"
%global php_min_ver     5.2.4

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{lib_name}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       A PHP client for Sentry

Group:         Development/Libraries
License:       BSD
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{url}/archive/%{github_commit}/%{name}-%{version}-%{github_commit}.tar.gz

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: %{_bindir}/phpunit
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 0.12.0)
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-hash
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-session
BuildRequires: php-spl
BuildRequires: php-zlib
%endif

%if %{with_cacert}
Requires:      ca-certificates
%endif
# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 0.12.0)
Requires:      php-curl
Requires:      php-date
Requires:      php-hash
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-session
Requires:      php-spl
Requires:      php-zlib

# Composer
Provides:      php-composer(raven/raven) = %{version}

%description
%{summary} (http://getsentry.com).


%prep
%setup -qn %{github_name}-%{github_commit}

%if %{with_cacert}
: Remove bundled cert
rm -rf lib/Raven/data
sed "/return.*cacert\.pem/s#.*#        return '%{_sysconfdir}/pki/tls/cert.pem';#" \
    -i lib/Raven/Client.php
%endif

: Create autoloader
(cat <<'AUTOLOAD'
<?php
/**
 * Autoloader created by %{name}-%{version}-%{release}
 */

require_once dirname(__FILE__) . '/Autoloader.php';
Raven_Autoloader::register();
AUTOLOAD
) | tee lib/Raven/autoload.php

: Update autoloader require in bin
sed "/require.*Autoloader/s:.*:require_once '%{phpdir}/Raven/Autoloader.php';:" \
    -i bin/raven


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/

mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/raven %{buildroot}%{_bindir}/


%check
%if %{with_tests}
: Update tests autoloader require
sed "/require.*Autoloader/s:.*:require_once '%{buildroot}%{phpdir}/Raven/Autoloader.php';:" \
    -i test/bootstrap.php

: Run tests
%{_bindir}/phpunit -v
%else
: Tests skipped
%endif


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.rst
%doc AUTHORS
%doc CHANGES
%doc composer.json
%{phpdir}/%{lib_name}
%{_bindir}/raven


%changelog
* Sat Jun 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.12.0-1
- Updated to 0.12.0 (RHBZ #1224010)
- Added autoloader

* Sun Apr 12 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.11.0-1
- Updated to 0.11.0 (BZ #1205685)

* Thu Sep 11 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.10.0-1
- Updated to 0.10.0 (BZ #1138284)

* Sun Aug 31 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.1-1
- Updated to 0.9.1 (BZ #1134284)
- %%license usage

* Sun Jun  8 2014 Remi Collet <remi@fedoraproject.org> 0.9.0-1
- backport 0.9.0 for remi repo

* Sat Jun 07 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.9.0-1
- Updated to 0.9.0 (BZ #1104557)
- Added php-composer(raven/raven) virtual provide
- Added option to build without tests

* Mon Jun  2 2014 Remi Collet <remi@fedoraproject.org> 0.8.0-2.20131209gitdac9333
- merge rawhide changes

* Fri May 30 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.8.0-3.20140519git2351d97
- Updated to latest snapshot
- Removed max PHPUnit dependency

* Mon Dec 30 2013 Remi Collet <remi@fedoraproject.org> 0.8.0-2.20131209gitdac9333
- backport 0.8.0 for remi repo.

* Mon Dec 30 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.8.0-2.20131209gitdac9333
- Updated to latest snapshot

* Sun Dec 29 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.8.0-1
- Updated to 0.8.0 (BZ #1037543)
- Spec cleanup

* Thu Oct  3 2013 Remi Collet <remi@fedoraproject.org> 0.7.1-1
- backport 0.7.1 for remi repo.

* Wed Oct 02 2013 Shawn Iwinski <shawn.iwinski@gmail.com> - 0.7.1-1
- Updated to 0.7.1

* Mon Jul  8 2013 Remi Collet <remi@fedoraproject.org> 0.6.1-1
- backport 0.6.1 for remi repo.

* Fri Jul 05 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.6.1-1
- Updated to 0.6.1 (BZ #981406)

* Fri Jun 07 2013 Remi Collet <remi@fedoraproject.org> 0.6.0-1
- backport 0.6.0 for remi repo.

* Fri Jun 07 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.6.0-1
- Updated to 0.6.0
- Removed tests sub-package

* Tue Feb 26 2013 Remi Collet <remi@fedoraproject.org> 0.5.1-1
- backport 0.5.1 for remi repo.

* Sun Feb 24 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.5.1-1
- Updated to upstream version 0.5.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Remi Collet <remi@fedoraproject.org> 0.4.0-2
- backport 0.4.0 for remi repo.

* Tue Jan 22 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.4.0-2
- Updated bin install from "install" to "install -pm 755"

* Mon Jan 21 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.4.0-1
- Updated to upstream version 0.4.0
- Fixed license
- Fixed build requires

* Fri Jan 18 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 0.3.1-1.20130117git60e91ac
- Initial package
