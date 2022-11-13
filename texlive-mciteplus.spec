Name:		texlive-mciteplus
Version:	31648
Release:	1
Summary:	Enhanced multiple citations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mciteplus
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mciteplus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mciteplus.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mciteplus LaTeX package is an enhanced reimplementation of
Thorsten Ohl's mcite package which provides support for the
grouping of multiple citations together as is often done in
physics journals. An extensive set of features provide for
other applications such as reference sublisting.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/mciteplus/IEEEtranM.bst
%{_texmfdistdir}/bibtex/bst/mciteplus/IEEEtranMN.bst
%{_texmfdistdir}/bibtex/bst/mciteplus/apsrevM.bst
%{_texmfdistdir}/bibtex/bst/mciteplus/apsrmpM.bst
%{_texmfdistdir}/tex/latex/mciteplus/mciteplus.sty
%doc %{_texmfdistdir}/doc/latex/mciteplus/README
%doc %{_texmfdistdir}/doc/latex/mciteplus/changelog.txt
%doc %{_texmfdistdir}/doc/latex/mciteplus/mciteplus_code.txt
%doc %{_texmfdistdir}/doc/latex/mciteplus/mciteplus_doc.pdf
%doc %{_texmfdistdir}/doc/latex/mciteplus/mciteplus_doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
