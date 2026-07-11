%global tl_name xetex-devanagari
%global tl_revision 34296

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	XeTeX input map for Unicode Devanagari
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/devanagari
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-devanagari.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-devanagari.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a map for use with Jonathan Kew's TECkit, to
translate Devanagari (encoded according to the Harvard/Kyoto convention)
to Unicode (range 0900-097F).

