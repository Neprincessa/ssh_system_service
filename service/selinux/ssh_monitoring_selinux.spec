# vim: sw=4:ts=4:et


%define relabel_files() \
restorecon -R /media/psf/Home/Documents/ssh/service/ssh-monitoring; \

%define selinux_policyver 3.13.1-192

Name:   ssh_monitoring_selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module for ssh_monitoring

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		http://HOSTNAME
Source0:	ssh_monitoring.pp
Source1:	ssh_monitoring.if
Source2:	ssh_monitoring_selinux.8


Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for ssh_monitoring.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/ssh_monitoring_selinux.8
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
%attr(0600,root,root) %{_datadir}/selinux/packages/ssh_monitoring.pp
%{_datadir}/selinux/devel/include/contrib/ssh_monitoring.if
%{_mandir}/man8/ssh_monitoring_selinux.8.*


%changelog
* Wed Jun  3 2020 YOUR NAME <YOUR@EMAILADDRESS> 1.0-1
- Initial version

