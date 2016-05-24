Name:         gpib_firmware
Version:      20080810
Release:      alt1

Summary:      Firmware for GPIB (IEEE 488) hardware.
Group:        System/Kernel and hardware
URL:          http://linux-gpib.sourceforge.net/
License:      Non-free

Packager:     Vladislav Zavjalov <slazav@altlinux.org>
Source:       %name-%version.tar

BuildPreReq:  kernel-headers-modules-un-def
Requires:     linux-gpib

%description
Firmware for GPIB (IEEE 488) hardware.

%prep
%setup -q

%build
%make install DESTDIR=%buildroot

%files
/usr/share/usb/agilent_82357a/*
/usr/share/usb/ni_gpib_usb_b/*

%changelog
