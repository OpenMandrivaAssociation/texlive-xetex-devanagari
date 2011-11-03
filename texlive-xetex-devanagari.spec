# revision 23223
# category Package
# catalog-ctan /macros/xetex/generic/devanagari
# catalog-date 2011-07-22 07:52:25 +0200
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-xetex-devanagari
Version:	0.4
Release:	1
Summary:	XeTeX input map for Unicode Devanagari
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/generic/devanagari
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-devanagari.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-devanagari.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package provides a map for use with Jonathan Kew's TECkit,
to translate Devanagari (encoded according to the Harvard/Kyoto
convention) to Unicode (range 0900-097F).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/README
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/devanagarinumerals.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/devanagarinumerals.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/harvardkyoto.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/harvardkyoto.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/iast.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/iast.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/velthuis-sanskrit.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/velthuis-sanskrit.tec
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/velthuis.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/xetex-devanagari/velthuis.tec
%doc %{_texmfdistdir}/doc/xetex/xetex-devanagari/changelog
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
