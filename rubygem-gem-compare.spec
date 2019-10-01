# Generated from gem-compare-0.0.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gem-compare

Name: rubygem-%{gem_name}
Version: 0.0.7
Release: 1%{?dist}
Summary: RubyGems plugin for comparing gem versions
License: MIT
URL: https://github.com/fedora-ruby/gem-compare
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildArch: noarch

%description
gem-compare is a RubyGems plugin that helps to compare
versions of the given gem.
It searches for differences in metadata as well as in files.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Itest:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test

%changelog
* Tue Oct 01 2019 Pavel Valena <pvalena@redhat.com> - 0.0.7-1
- Initial package
