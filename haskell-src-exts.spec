%define hs_package haskell-src-exts

Summary:	An extension of the standard haskell-src package
Name:		%{hs_package}
Version: 	1.3.3
Release: 	%mkrel 1
Source0: 	http://www.cs.chalmers.se/~d00nibro/haskell-src-exts/%{hs_package}-%{version}.tar.gz
License: 	GPL
Group:		Development/Other
Url: 		http://www.cs.chalmers.se/~d00nibro/haskell-src-exts/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	ghc
BuildRequires:	haskell-macros
Buildrequires:	happy
BuildRequires:	cpphs >= 1.3
Requires:	ghc

%description
Haskell-Source with eXtensions (HSX, haskell-src-exts) is an extension of the
standard haskell-src package, and handles most common syntactic extensions to
Haskell, including:

  * Multi-parameter type classes with functional dependencies
  * Empty data declarations
  * GADTs
  * Implicit parameters (ghc and hugs style)
  * Template Haskell (broken for 6.4, needs redoing)

and a few more. Apart from these standard extensions, it also handles regular
patterns as per the HaRP extension as well as HSP-style embedded XML syntax
(HSP release imminent).

%prep
%setup -q -n %{hs_package}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%install
rm -rf $RPM_BUILD_ROOT
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*
%{_docdir}/%{name}-%{version}
%_cabal_rpm_files
