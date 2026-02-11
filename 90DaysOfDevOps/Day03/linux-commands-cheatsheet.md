Linux Commands Cheat Sheet


1. Process Management
---

##### 

'ps aux' – List all running processes



'top' – Real-time CPU and memory usage



'htop' – Enhanced process viewer (interactive)



'kill PID' – Send signal to stop a process



'kill -9 PID' – Force kill a stuck process



'nice -n 10 command' – Start process with priority



'uptime' – Check system load and running time

##### 

##### 2\. File System \& Disk

##### 

'ls -lah' – List files with permissions and size



'cd /path' – Change directory



'pwd' – Show current directory



'df -h' – Disk space usage



'du -sh folder' – Folder size



'cp file1 file2' – Copy file



'mv old new' – Move or rename file



'rm -rf folder' – Delete files/folders



'find / -name file' – Search files



'chmod 755 file' – Change file permissions



'chown user:group file' – Change ownership

##### 

##### 3\. Logs \& Monitoring

##### 

'journalctl' – View system logs



'journalctl -u service' – Logs for a service



'tail -f file.log' – Live log monitoring



'less file.log' – Read large log files



'grep "error" file.log' – Search logs



##### 4\. Networking \& Troubleshooting

##### 

'ping google.com' – Test network connectivity



'ip addr' – Show IP addresses



'ss -tuln' – Check listening ports



'curl http://url

' – Test HTTP endpoint



'dig google.com' – DNS lookup

##### 

##### 5\. Service Management (systemd)

##### 

'systemctl status service' – Check service status



'systemctl start service' – Start service



'systemctl stop service' – Stop service



'systemctl restart service' – Restart service



'systemctl enable service' – Enable on boot

