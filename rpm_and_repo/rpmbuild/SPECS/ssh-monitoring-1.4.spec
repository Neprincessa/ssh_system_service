%define relabel_files() \
restorecon -R -v /usr/bin; \
restorecon -R -v /usr/lib/systemd/system; \

%define selinux_policyver 3.13.1-266

Name:           ssh-monitoring
Version:        1.4
Release:        1%{?dist}
Summary:        Session Monitoring Service

Group:          ssh-monitoring
License:        GPL
URL:            https://github.com/Neprincessa/ssh_system_service
Source0:        %{name}-%{version}.tar.gz
Source1:	ssh-monitoring-1.3/ssh_monitoring.pp
Source2:	ssh-monitoring-1.3/ssh_monitoring.if
Source3:	ssh-monitoring-1.3/my-logger.pp
Source4:	ssh-monitoring-1.3/my-notifysend.pp
Source5:	ssh-monitoring-1.3/my-ps.pp
Source6:	ssh-monitoring-1.3/my-sshmonitoring.pp

BuildRequires:  /bin/mkdir, /bin/cp, /bin/rm, /bin/sudo, systemd, libnotify-devel, selinux-policy-devel
Requires:       /bin/bash, /usr/bin/ps, /usr/bin/logger, /usr/bin/awk, /usr/bin/echo, /usr/bin/grep, /usr/bin/tr, /usr/bin/cut
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python libselinux-utils
BuildArch: noarch

%description
Session Monitoring 

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}%{_mandir}/man8
install -m 755 ssh-monitoring\.sh %{buildroot}%{_bindir}/
install -m 755 ssh-monitoring-lib.sh %{buildroot}%{_bindir}/
install -m 644 ssh-monitoring.service %{buildroot}/etc/systemd/system/
install -m 644 ssh-monitoring.8.gz %{buildroot}%{_mandir}/man8/
# Install policy modules
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE5} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE6} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}/etc/selinux/targeted/contexts/users/

%post
semodule -n -i %{_datadir}/selinux/packages/ssh_monitoring.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files
fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r ssh_monitoring
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files
    fi;
fi;
exit 0

%files
%{_bindir}/ssh-monitoring.sh
%{_bindir}/ssh-monitoring-lib.sh
/etc/systemd/system/ssh-monitoring.service
%{_mandir}/man8/ssh-monitoring.8.gz
%defattr(-,root,root,0755)
%attr(0600,root,root) 
%{_datadir}/selinux/packages/ssh_monitoring.pp
%{_datadir}/selinux/packages/my-logger.pp
%{_datadir}/selinux/packages/my-ps.pp
%{_datadir}/selinux/packages/my-notifysend.pp
%{_datadir}/selinux/packages/my-sshmonitoring.pp
%{_datadir}/selinux/devel/include/contrib/ssh_monitoring.if

%changelog
* Thu Jun 4 2020 <cheraten>
- Added %{_bindir}/ssh-monitoring-1.3.spec
