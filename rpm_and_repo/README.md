### Сборка RPM пакета и создание репозитория

1. `cd ~`
2. `rpmdev-setuptree`
3. `cd ~/rpmbuild/SOURCES`
4. `mkdir ssh-monitoring-lastver`
5. `cp ~/ssh_system_service/rpm_and_repo/rpmbuild/SOURCES/ssh-monitoring-lastver/* ./ssh-monitoring-lastver`
6. `tar -cvzf ssh-monitoring-lastver.tar.gz ssh-monitoring-lastver`
7. `cd ../SPECS`
8. `~/ssh_system_service/rpm_and_repo/rpmbuild/SPECS/ssh-monitoring-lastver.spec ./`
9. `rpmbuild --ba ssh-monitoring-lastver.spec`
10. `sudo rpm -addsign ~/rpmbuild/RPMS/noarch/ssh-monitoring-lastver-1.el7.noarch.rpm`
11. `sudo mkdir -p /var/www/html/ssh-monitoring`
12. `sudo cp ~/rpmbuild/RPMS/noarch/ssh-monitoring-lastver-1.el7.noarch.rpm /var/www/html/ssh-monitoring`
13. `sudo createrepo -v /var/www/html/ssh-monitoring`
14. `sudo mv ~/ssh_system_service/rpm_and_repo/rpmbuild/RPM-GPG-KEY-cheraten3 /var/www/html/gpg-key`
15. `sudo cp ~/ssh_system_service/rpm_and_repo/ssh-monitoring.repo /etc/yum.repos.d`
16. `sudo yum update`
