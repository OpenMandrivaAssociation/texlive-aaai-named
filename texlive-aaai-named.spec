%global tl_name aaai-named
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	BibTeX style for AAAI
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/aaai-named.bst
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aaai-named.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A BibTeX style derived from the standard master, presumably for use with
the aaai package.

