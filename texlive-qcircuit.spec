Name:		texlive-qcircuit
Version:	48400
Release:	2
Summary:	Macros to generate quantum ciruits
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/qcircuit
License:	gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qcircuit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qcircuit.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports those within the quantum information
community who typeset quantum circuits, using xy-pic package,
offering macros designed to help users generate circuits.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/qcircuit
%doc %{_texmfdistdir}/doc/latex/qcircuit

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
