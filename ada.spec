%define major 4
%define libname %mklibname ada
%define devname %mklibname ada -d

Name: ada
Version: 4.0.0
Release: 1
Source0: https://github.com/ada-url/ada/archive/refs/tags/v%{version}.tar.gz
Summary: C++ URL parser library
URL: https://github.com/ada-url/ada
License: Apache-2.0
Group: System/Libraries
BuildSystem: cmake
BuildOption: -DADA_TESTING:BOOL=OFF
BuildOption: -DADA_TOOLS:BOOL=OFF
BuildOption: -DADA_BENCHMARKS:BOOL=OFF
BuildOption: -DADA_USE_SIMDUTF:BOOL=OFF
BuildOption: -DBUILD_SHARED_LIBS:BOOL=ON
BuildRequires: cmake

%patchlist

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

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
