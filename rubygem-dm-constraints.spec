# Generated from dm-constraints-1.2.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	dm-constraints

Summary:	DataMapper plugin constraining relationships
Name:		rubygem-%{rbname}

Version:	1.2.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/datamapper/dm-constraints
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
DataMapper plugin constraining relationships

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_mapper/constraints/adapters/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_mapper/constraints/migrations/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_mapper/constraints/relationship/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/data_mapper/constraints/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
