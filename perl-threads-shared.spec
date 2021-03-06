%define upstream_name    threads-shared
%define upstream_version 1.58
Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

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

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/*
