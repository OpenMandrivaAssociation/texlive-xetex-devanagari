Name:		texlive-xetex-devanagari
Version:	34296
Release:	2
Summary:	XeTeX input map for Unicode Devanagari
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/devanagari
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-devanagari.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-devanagari.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a map for use with Jonathan Kew's TECkit,
to translate Devanagari (encoded according to the Harvard/Kyoto
convention) to Unicode (range 0900-097F).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari
%doc %{_texmfdistdir}/doc/xetex/xetex-devanagari

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
