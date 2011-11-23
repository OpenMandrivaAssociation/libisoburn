%define	version	1.1.8
%define	rel	1

%define	major	1
%define	libname	%mklibname	isoburn	%major
%define	devname	%mklibname	isoburn	-d

Name:		libisoburn
Version:	1.1.8
Summary:	Enables creation and expansion of ISO-9660 filesystems on all CD/DVD media supported by libburn
Release:	1
Source:		http://downloads.sourceforge.net/cdemu/%name-%version.tar.gz
Group:		System/Libraries
License:	GPLv2+
URL:		http://libburnia-project.org

BuildRequires:	libburn-devel >= 1.1.6
BuildRequires:	libacl-devel
BuildRequires:	glib2-devel
BuildRequires:	doxygen
BuildRequires:	libisofs-devel >= 1.1.6
BuildRequires:	zlib-devel


%package -n %libname
Summary:	CD-ROM image access library - shared library
Group:		System/Libraries


%description -n %libname
Shared libraries of libisoburn for software using it.

%description
libisoburn is a frontend for libraries libburn and libisofs which enables creation and expansion of ISO-9660 filesystems on all CD/DVD/BD media supported by libburn. 
This includes media like DVD+RW, which do not support multi-session management on media level and even plain disk files or block devices.
The price for that is thorough specialization on data files in ISO-9660 filesystem images. So libisoburn is not suitable for audio 
(CD-DA) or any other CD layout which does not entirely consist of ISO-9660 sessions.

%package -n %devname
Summary:	CD-ROM image access library - development headers
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libisoburn-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %devname
The libisoburn-devel package contains libraries and header files for
developing applications that use libisoburn.


%package -n xorriso-isoburn
Summary:	ISO-9660 and Rock Ridge image manipulation tool
Group:		Archiving/Cd burning
URL:		http://scdbackup.sourceforge.net/xorriso_eng.html
Requires:	%{libname} = %{version}-%{release}

%description -n xorriso-isoburn
Xorriso is a program which copies file objects from POSIX compliant
filesystems into Rock Ridge enhanced ISO-9660 filesystems and allows
session-wise manipulation of such filesystems. It can load management
information of existing ISO images and it writes the session results
to optical media or to filesystem objects. Vice versa xorriso is able
to copy file objects out of ISO-9660 filesystems.

Filesystem manipulation capabilities surpass those of mkisofs. Xorriso
is especially suitable for backups, because of its high fidelity of
file attribute recording and its incremental update sessions. Optical
supported media: CD-R, CD-RW, DVD-R, DVD-RW, DVD+R, DVD+R DL, DVD+RW,
DVD-RAM, BD-R and BD-RE. 

%prep
%setup -q

%build
touch NEWS

autoreconf -fi

%configure --disable-static
%make
doxygen doc/doxygen.conf

%install
%makeinstall_std

rm -f %{buildroot}/%{_libdir}/{*.la,*.a}


%files -n %libname
%doc AUTHORS COPYING COPYRIGHT README ChangeLog
%{_libdir}/%{name}*.so.*

%files -n %devname
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}*.pc

%files -n xorriso-isoburn
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorrisofs
%{_mandir}/man1/xorriso.1*
%{_mandir}/man1/xorrisofs.1*
%{_mandir}/man1/xorrecord.1*
%{_infodir}/xorriso.info*
%{_infodir}/xorrecord.info*
%{_infodir}/xorrisofs.info*
