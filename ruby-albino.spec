
%define gitrev 27e2eba
%define gitauthor github
%define gitname albino

Summary:	Ruby wrapper for the Pygments syntax highlighter
Name:		ruby-albino
Version:	1.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{gitname}-%{gitrev}.tar.gz
# Source0-md5:	37e23e2759fa95c01c89258acf61a27a
URL:		http://github.com/github/albino
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby wrapper for the Pygments syntax highlighter. 

%prep
%setup -q -n %{gitauthor}-%{gitname}-%{gitrev}
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/usr/lib/ruby/1.8/albino.rb
