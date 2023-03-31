Name:		texlive-visualpstricks
Version:	39799
Release:	2
Summary:	Visual help for PSTricks based on images with minimum text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/visualpstricks
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/visualpstricks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/visualpstricks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Visual help for PSTricks based on images with minimum text. One
image per command or per parameter.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/visualpstricks

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
