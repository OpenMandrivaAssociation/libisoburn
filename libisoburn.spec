%define major 1
%define libname %mklibname isoburn %{major}
%define devname %mklibname isoburn -d

Summary:	Enables creation and expansion of ISO-9660 filesystems
Name:		libisoburn
Version:	1.5.4
Release:	1
Group:		System/Libraries
License:	GPLv2+
Url:		https://dev.lovelyhq.com/libburnia/libisoburn
Source0:	https://dev.lovelyhq.com/libburnia/libisoburn/archive/release-%{version}.tar.gz

BuildRequires:	doxygen
BuildRequires:	pkgconfig(libacl)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libburn-1) >= %{version}
BuildRequires:	pkgconfig(libisofs-1) >= %{version}
BuildRequires:	pkgconfig(zlib)

%package -n %{libname}
Summary:	CD-ROM image access library - shared library
Group:		System/Libraries

%description -n %{libname}
Shared libraries of libisoburn for software using it.

%description
libisoburn is a frontend for libraries libburn and libisofs which
enables creation and expansion of ISO-9660 filesystems on all CD/DVD/BD
media supported by libburn.
This includes media like DVD+RW, which do not support multi-session management
on media level and even plain disk files or block devices.
The price for that is thorough specialization on data files
in ISO-9660 filesystem images. So libisoburn is not suitable for audio 
(CD-DA) or any other CD layout which does not entirely consist
of ISO-9660 sessions.

%package -n %{devname}
Summary:	CD-ROM image access library - development headers
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Provides:	libisoburn-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
The libisoburn-devel package contains libraries and header files for
developing applications that use libisoburn.

%package -n xorriso
Summary:	ISO-9660 and Rock Ridge image manipulation tool
Group:		Archiving/Cd burning
Requires:	%{libname} = %{EVRD}
# (tpg) looks like these two are needed
Requires:	%{_lib}isofs6 >= %{version}
Requires:	%{_lib}burn4 >= %{version}

Obsoletes:	xorriso-isoburn < %{EVRD}
Provides:	xorriso-isoburn = %{EVRD}

%description -n xorriso
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

%package -n xorriso-tcltk
Summary:	TCL/Tk frontend for the Xorriso ISO-9660 image manipulation tool
Group:		Archiving/Cd burning
Requires:	xorriso = %{EVRD}

%description -n xorriso-tcltk
A TCL/Tk based frontend for the Xorriso ISO-9660 image manipulation tool.

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
%autosetup -p1 -n %{name}
%configure --enable-pkg-check-modules

%build
%make_build LIBS='-lpthread -lreadline'
doxygen doc/doxygen.conf

%install
%make_install

%files -n %{libname}
%{_libdir}/%{name}*.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING COPYRIGHT README ChangeLog
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}*.pc

%files -n xorriso
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorriso-dd-target
%{_bindir}/xorrisofs
%doc %{_mandir}/man1/xorriso.1*
%doc %{_mandir}/man1/xorriso-dd-target.1*
%doc %{_mandir}/man1/xorrisofs.1*
%doc %{_mandir}/man1/xorrecord.1*
%doc %{_infodir}/xorriso.info*
%doc %{_infodir}/xorriso-dd-target.info*
%doc %{_infodir}/xorrecord.info*
%doc %{_infodir}/xorrisofs.info*

%files -n xorriso-tcltk
%{_bindir}/xorriso-tcltk
%doc %{_mandir}/man1/xorriso-tcltk.1.*
%doc %{_infodir}/xorriso-tcltk.info*
