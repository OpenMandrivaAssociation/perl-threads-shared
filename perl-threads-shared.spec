
%define realname   threads-shared
%define version    1.27
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl extension for sharing data structures between threads
Source:     http://www.cpan.org/modules/by-module/threads/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
BuildRequires: perl(warnings)



%description
By default, variables are private to each thread, and each newly created
thread gets a private copy of each existing variable. This module allows
you to share variables across different threads (and pseudo-forks on
Win32). It is used together with the the threads manpage module.

This module supports the sharing of the following data types only: scalars
and scalar refs, arrays and array refs, and hashes and hash refs.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


