%define upstream_name    HTML-Template-Pluggable
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Extends HTML::Template with plugin support
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Trigger)
BuildRequires:	perl(HTML::Template)
BuildRequires:	perl(Regexp::Common)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(CGI)
BuildArch:	noarch

%description
By adding support for this dot notation to the HTML::Template manpage, the
programmers' job of sending data to the template is easier, and designers
have easier access to more data to display in the template, without
learning any more tag syntax.

EXAMPLES
Class::DBI integration
    the Class::DBI manpage accessors can be used in the template. If the
    accessor is never called in the template, that data doesn't have to be
    loaded.

    In the code:

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
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.170.0-2mdv2011.0
+ Revision: 654826
- add br
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 624903
- import perl-HTML-Template-Pluggable

