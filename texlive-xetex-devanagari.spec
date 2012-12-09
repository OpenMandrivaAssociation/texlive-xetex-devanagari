# revision 23223
# category Package
# catalog-ctan /macros/xetex/generic/devanagari
# catalog-date 2011-07-22 07:52:25 +0200
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-xetex-devanagari
Version:	0.4
Release:	2
Summary:	XeTeX input map for Unicode Devanagari
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/generic/devanagari
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-devanagari.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-devanagari.doc.tar.xz
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 757596
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 719931
- texlive-xetex-devanagari
- texlive-xetex-devanagari
- texlive-xetex-devanagari

