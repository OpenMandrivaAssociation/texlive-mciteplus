%global tl_name mciteplus
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Enhanced multiple citations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mciteplus
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mciteplus.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mciteplus.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mciteplus LaTeX package is an enhanced reimplementation of Thorsten
Ohl's mcite package which provides support for the grouping of multiple
citations together as is often done in physics journals. An extensive
set of features provide for other applications such as reference
sublisting.

