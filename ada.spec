%define major 2
%define libname %mklibname ada
%define devname %mklibname ada -d

Name: ada
Version: 2.9.2
Release: 2
Source0: https://github.com/ada-url/ada/archive/refs/tags/v%{version}.tar.gz
Source1: https://github.com/cpm-cmake/CPM.cmake/archive/refs/tags/v0.38.6.tar.gz
Summary: C++ URL parser library
URL: https://github.com/ada-url/ada
License: Apache-2.0
Group: System/Libraries
BuildSystem: cmake
BuildOption: -DADA_TESTING:BOOL=OFF
BuildOption: -DCPM_USE_LOCAL_PACKAGES:BOOL=ON
BuildOption: -DCPM_LOCAL_PACKAGES_ONLY:BOOL=ON
BuildOption: -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON
BuildOption: -DCPM_SOURCE_CACHE=$(pwd)/../CPM.cmake-0.38.6
BuildRequires: cmake(fmt)
BuildRequires: cmake(cxxopts)
BuildRequires: git-core

%patchlist
ada-2.9.0-no-downloads.patch

%description
C++ URL parser library

%package -n %{libname}
Summary: C++ URL parser library
Group: System/Libraries

%description -n %{libname}
C++ URL parser library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep -a
# see cmake/CPM.cmake for what needs to be done here to
# prevent a download
tar xf %{S:1}
mkdir CPM.cmake-0.38.6/cpm
cp CPM.cmake-0.38.6/cmake/CPM.cmake CPM.cmake-0.38.6/cpm/CPM_0.38.6.cmake

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
