# SSH monitoring service
1. Copy service to /etc/systemd/sytem
2. Copy script to в /usr/bin/ + make executable
3. systemctl daemon-reload
4. systemctl enable 
5. sudo systemctl start monitoring_ssh_service.service 
6.sudo systemctl status monitoring_ssh_service.service
7. systemctl stop monitoring_ssh_service.service - остановка
8. journalctl -f -u monitoring_ssh_service.service - получаем выводы сервиса
