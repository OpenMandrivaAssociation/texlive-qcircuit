%global tl_name qcircuit
%global tl_revision 48400

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6.0
Release:	%{tl_revision}.1
Summary:	Macros to generate quantum ciruits
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/qcircuit
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qcircuit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/qcircuit.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports those within the quantum information community who
typeset quantum circuits, using xy-pic package, offering macros designed
to help users generate circuits.

