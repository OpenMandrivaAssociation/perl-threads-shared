%define upstream_name    threads-shared
%define upstream_version 1.46
Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	1

Summary:    Perl extension for sharing data structures between threads
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/J/JD/JDHEDDEN/threads-shared-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::testlib)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(strict)
BuildRequires: perl(threads)
Provides: perl(threads::shared)

%description
By default, variables are private to each thread, and each newly created
thread gets a private copy of each existing variable. This module allows
you to share variables across different threads (and pseudo-forks on
Win32). It is used together with the the threads manpage module.

This module supports the sharing of the following data types only: scalars
and scalar refs, arrays and array refs, and hashes and hash refs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.360.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Mar 07 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.360.0-1
+ Revision: 642415
- new version

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.340.0-1mdv2011.0
+ Revision: 596733
- update to 1.34

* Sat Sep 18 2010 Shlomi Fish <shlomif@mandriva.org> 1.330.0-4mdv2011.0
+ Revision: 579576
- Bump the rel number so the PERL5LIB will be visible on the newer Perl

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.330.0-3mdv2011.0
+ Revision: 562465
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.330.0-2mdv2011.0
+ Revision: 555203
- rebuild for 5.12

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1.330.0-1mdv2010.1
+ Revision: 518086
- update to 1.33

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.320.0-1mdv2010.1
+ Revision: 460780
- update to 1.32

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.310.0-3mdv2010.0
+ Revision: 421022
- rebuild
- rebuild
- update to 1.31

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.310.0-2mdv2010.0
+ Revision: 417019
- force rebuild
- update to 1.31

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.290.0-1mdv2010.0
+ Revision: 392734
- update to 1.29
- using %%perl_convert_version
- fixed license field

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.28-1mdv2010.0
+ Revision: 372410
- update to new version 1.28
- update source url

* Sat Jan 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.27-1mdv2009.1
+ Revision: 330691
- and yet another legit provides stripped by importer... sigh
- import perl-threads-shared


* Sat Jan 17 2009 cpan2dist 1.27-1mdv
- initial mdv release, generated with cpan2dist





