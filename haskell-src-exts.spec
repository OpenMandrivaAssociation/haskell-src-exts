%define hs_package haskell-src-exts
%define ghc_version %(rpm -q ghc | cut -d- -f2)

Summary:	An extension of the standard haskell-src package
Name:		%{hs_package}
Version: 	0.2
Release: 	%mkrel 2
Source0: 	http://www.cs.chalmers.se/~d00nibro/haskell-src-exts/%{hs_package}-%{version}.tar.bz2
License: 	GPL
Group:		Development/Other
Url: 		http://www.cs.chalmers.se/~d00nibro/haskell-src-exts/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	ghc = %{ghc_version}
Buildrequires:	happy
Requires:	ghc = %{ghc_version}

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
%setup -q -n %{hs_package}

%build
cd src/haskell-src-exts
runhaskell Setup configure --ghc -v --prefix=%{_prefix}
runhaskell Setup build -v

# generate register and unregister scripts
runhaskell Setup register --gen-script
runhaskell Setup unregister --gen-script

%install
rm -rf $RPM_BUILD_ROOT

cd src/haskell-src-exts
runhaskell Setup copy  --copy-prefix=$RPM_BUILD_ROOT/%{_prefix}

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp register.sh $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp unregister.sh $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/*
%{_datadir}/*
#%doc Abrechnung.lhs dot.lhs Tests.lhs

%post -p %{_datadir}/%{name}/register.sh

%preun -p %{_datadir}/%{name}/unregister.sh

