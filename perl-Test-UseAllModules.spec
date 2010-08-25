%define upstream_name    Test-UseAllModules
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Do use_ok() for all modules MANIFESTed
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::Manifest)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
I'm sick of writing 00_load.t (or something like that) that'll do use_ok()
for every module I write. I'm sicker of updating 00_load.t when I add
another file to the distro. This module reads MANIFEST to find modules to
be tested and does use_ok() for each of them. Now all you have to do is
update MANIFEST. You don't have to modify the test any more (hopefully).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


