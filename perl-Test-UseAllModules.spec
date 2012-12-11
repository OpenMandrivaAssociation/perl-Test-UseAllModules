%define upstream_name    Test-UseAllModules
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Do use_ok() for all modules MANIFESTed
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::Manifest)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
I'm sick of writing 00_load.t (or something like that) that'll do use_ok()
for every module I write. I'm sicker of updating 00_load.t when I add
another file to the distro. This module reads MANIFEST to find modules to
be tested and does use_ok() for each of them. Now all you have to do is
update MANIFEST. You don't have to modify the test any more (hopefully).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 657473
- rebuild for updated spec-helper

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1
+ Revision: 646398
- update to new version 0.13

* Wed Aug 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 573151
- import perl-Test-UseAllModules

