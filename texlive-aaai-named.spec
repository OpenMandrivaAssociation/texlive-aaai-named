Name:		texlive-aaai-named
Version:	52470
Release:	2
Summary:	BibTeX style for AAAI
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aaai-named
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aaai-named.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A BibTeX style derived from the standard master, presumably for
use with the aaai package.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/aaai-named

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
