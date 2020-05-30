Name:           ssh-monitoring
Version:        1.0
Release:        1%{?dist}
Summary:        Session Monitoring Service

Group:          ssh-monitoring
License:        GPL
URL:            https://github.com/Neprincessa/ssh_system_service
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  /bin/mkdir, /bin/cp, /bin/rm, /bin/sudo, systemd, libnotify-devel
Requires:       /bin/bash, /usr/bin/ps, /usr/bin/logger, /usr/bin/awk, /usr/bin/echo, /usr/bin/grep, /usr/bin/tr, /usr/bin/cut
BuildArch: noarch

%description
Session Monitoring 

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}/etc/systemd/system/
install -m 755 ssh-monitoring\.sh %{buildroot}%{_bindir}/
install -m 755 ssh-monitoring-lib.sh %{buildroot}%{_bindir}/
install -m 644 ssh-monitoring.service %{buildroot}/etc/systemd/system/

%files
%{_bindir}/ssh-monitoring.sh
%{_bindir}/ssh-monitoring-lib.sh
/etc/systemd/system/ssh-monitoring.service
%defattr(-,root,root,0755)

%changelog
* Fri May 29 2020 <cheraten>
- Added %{_bindir}/ssh-monitoring-1.0.spec
