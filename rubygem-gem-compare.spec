# Generated from gem-compare-0.0.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gem-compare

Name: rubygem-%{gem_name}
Version: 0.0.7
Release: 1.1%{?dist}
Summary: RubyGems plugin for comparing gem versions
License: MIT
URL: https://github.com/fedora-ruby/gem-compare
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# gemfiles folder is not included
# https://github.com/fedora-ruby/gem-compare/pull/19
# git clone git@github.com:fedora-ruby/gem-compare.git --no-checkout
# cd gem-compare && git archive -v -o gem-compare-0.0.7-gemfiles.txz v0.0.7 test/gemfiles
Source1: %{gem_name}-%{version}-gemfiles.txz
Patch0: 0001-Fixup-tests.patch

# Due to internal resolver requirement in Ruby 2.6
Requires: rubygem(bundler)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(rainbow)
BuildRequires: rubygem(curb)
BuildRequires: rubygem(diffy)
BuildRequires: rubygem(gemnasium-parser)
BuildRequires: rubygem(minitest)
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
%setup -q -n %{gem_name}-%{version} -b1

%patch0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}

ln -s {%{_builddir}/,}test/gemfiles
ruby -Itest:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test

%changelog
* Tue Oct 01 2019 Pavel Valena <pvalena@redhat.com> - 0.0.7-1
- Initial package
