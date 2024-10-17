%define name iwlwifi-135-ucode
%define version 18.168.6.1
%define release 2

Summary: Intel PRO/Wireless N 105 microcode
Name: %{name}
Version: %{version}
Release: %{release}
Source: http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-135-ucode-%{version}.tgz
License: Proprietary
Group: System/Kernel and hardware
Url: https://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-135-*.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless N 135 Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q

%build

%install
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/

%files
%doc LICENSE.* README.*
/lib/firmware/*.ucode


