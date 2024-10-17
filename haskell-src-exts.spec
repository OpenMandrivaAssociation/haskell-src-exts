%global debug_package %{nil}
#% define _cabal_setup Setup.lhs
#% define _no_haddock 1
%define module haskell-src-exts
Name:           %{module}
Version:        1.13.5
Release:        1
Summary:        Manipulating Haskell source: abstract syntax, lexer, parser, and pretty-printer
Group:          Development/Other
License:        BSD
URL:            https://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
buildrequires:  cpphs happy
Requires(pre):  ghc
requires(pre):  cpphs happy

%description
Haskell-Source with Extensions (HSE, haskell-src-exts) is an extension of the
standard haskell-src package, and handles most registered syntactic extensions
to Haskell, including:
* Multi-parameter type classes with functional dependencies
* Indexed type families (including associated types)
* Empty data declarations
* GADTs
* Implicit parameters
* Template Haskell
and a few more. All extensions implemented in GHC are supported.
Apart from these standard extensions, it also handles regular patterns as per
the HaRP extension as well as HSX-style embedded XML syntax.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

#% check
#% _cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files



