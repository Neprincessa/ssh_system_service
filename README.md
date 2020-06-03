### Создание политики SELinux

1. Сгенерировать шаблон модуля политики SELinux:

`sepolicy generate --init ssh_monitoring`

Будут созданы 5 файлов:

-Type Enforcing File ssh_monitoring.te; 

-Interface File ssh_monitoring.if; 

-File Context ssh_monitoring.fc; 

-RPM Spec File ssh_monitoring_selinux.spec; 

-Shell File ssh_monitoring.sh

2. Запустить скрипт ssh_monitoring.sh:

`sudo ./ssh_monitoring.sh`

Будет создан модуль политики SELinux - файл ssh_monitoring.pp

3. Добавить политику в список системных модулей:

`semodule -i ssh_monitoring.pp`

4. Изменить контекст безопасности (тип) сервиса : 

`sudo chcon -t ssh_monitoring_exec_t /usr/bin/ssh-monitoring`

Посмотреть изменившийся контекст можно командой: 

`ps -eZ | grep ssh-monitoring`

![](https://sun1-99.userapi.com/NgBV9yEECpgx71EZmFH34TF6ofKNJtkP3oh4Kg/rvyt1f8yy98.jpg)

5.  Проверить работу сервиса: 

Подключиться к ssh от имени другого пользователя cheraten1 и переключиться обратно на cheraten:

![](https://sun1-96.userapi.com/WOca_Rpg1t-ki21X8V9VU6ZhHGnl-fuP_RJ79Q/0Q-iAvySYTg.jpg)

Посмотреть запись в файле /var/log/messages: 

![](https://sun9-50.userapi.com/Sm65W38UyAn_xZ-uwF59BwsVe3PV61f0CfVW7A/C0n9RYijLgo.jpg)

![](https://sun9-72.userapi.com/PcwRn9YLQbS7cPUVJmi68v5OvZmZ1tXLv-HI9w/wOvk0Sy6_ds.jpg)

При появлении сообщений в файле /var/log/messages о необходимости создания дополнительных модулей политики, выполнить предложенные команды.

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

### Cоздание gpg ключа

1. `gpg --gen-key`

![](https://sun1-19.userapi.com/IxTaETmLnpp2TQxjRJOlsl67ZkR0PZUPqOdbBg/rOUXM9RI-B4.jpg)

![](https://sun1-95.userapi.com/3MqxGl6d9x5YnPifAsn4tw5lH87GE8sqkJuyaQ/KSr2UET2KQY.jpg)

2. `gpg2 --export -a 'cheraten3' > ~/rpmbuild/RPM-GPG-KEY-cheraten3`

3. `vi ~/.rpmmacros`

![](https://sun1-96.userapi.com/BLZSoy_qCRdC4dTc5YYKfXyKasUgvLoJGrMEFg/Ol8k2qC9QzE.jpg)

4. `gpg --export --armor 7A36FC6D  > /tmp/gpg-key`

5. `cp /tmp/gpg-key /var/www/html/`

### Демонстрация работы сервиса

1. `sudo yum install ssh-monitoring`
2. `sudo systemctl start ssh-monitoring`
3. `ps -eZ | grep ssh-monitoring`

Сервис работает в собственном домене.

![](https://sun1-89.userapi.com/FiXlLQIYpdQlhLnrwd-1kaDih6l7XuvmVLJHuA/TbPddxQDKQM.jpg)

4. `sudo systemctl restart ssh-monitoring`

5. `journalctl -f -u ssh-monitoring`

Перезапуск сервиса.

![](https://sun1-47.userapi.com/Z_D0brtaNUemK9lB2RCy0Q1yasRkRMf2tRf3bg/_i7Qa4e20iE.jpg)

Запуск сервиса (сообщения в /var/log/messages)

![](https://sun1-24.userapi.com/X7F-hvXeN33BgXDyYC61_BMKl45h8C5Iqy08Hw/OCs3ngFuULE.jpg)

6. Подключение пользователя cheraten1 в систему по ssh

![](https://sun9-67.userapi.com/rurpc4FcLs_drGBC6EgVZNUp3XErJcqAxBc2Ww/WwG62pUfFlo.jpg)

Сообщения в /var/log/messages:

![](https://sun9-71.userapi.com/GIXqZtUmRZtyplW0v-kZmS_9kXBwkjaAAQx5sQ/uhlLjmR4-sc.jpg)

7. Обработка сигнала USR1:

![](https://sun9-6.userapi.com/_cs9lbK-xs9S63aPOn3586q6TtmXWhfJ5mTZWA/uPIgpgs0zuo.jpg)

![](https://sun9-17.userapi.com/fV3Us2ksMmzeeT7jgvr_CpwhQMRKW32A06GQqQ/1ygDYYpRJRU.jpg)

8. Демонстрация man страницы

![](https://sun1-93.userapi.com/cMysp4JZOrN3BGJ2S6sqAdO_reDBPmuZENqJWw/At1EGKtEPCg.jpg)

