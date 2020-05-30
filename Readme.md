# SSH monitoring service
1. Copy service to /etc/systemd/sytem
2. Copy script to в /usr/bin/ + make executable
3. systemctl daemon-reload
4. sudo systemctl enable ssh-monitoring.service
5. sudo systemctl start ssh-monitoring.service
6. sudo systemctl status ssh-monitoring.service
7. systemctl stop ssh-monitoring.service - остановка
8. journalctl -f -u ssh-monitoring.service - получаем выводы сервиса

