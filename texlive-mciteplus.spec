# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mciteplus
# catalog-date 2008-09-30 16:07:39 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-mciteplus
Version:	1.1
Release:	1
Summary:	Enhanced multiple citations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mciteplus
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mciteplus.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mciteplus.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The mciteplus LaTeX package is an enhanced reimplementation of
Thorsten Ohl's mcite package which provides support for the
grouping of multiple citations together as is often done in
physics journals. An extensive set of features provide for
other applications such as reference sublisting.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
