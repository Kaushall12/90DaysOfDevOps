#### Linux Practice – Processes and Services







##### Process Checks

###### 

###### 1\. Check running processes



Command:

'ps aux | head'



Output:

Shows top running processes with USER, PID, %CPU, %MEM.



Observation:

System processes like systemd and bash are running with low CPU usage.



###### 2\. Real-time monitoring



Command:

'top'



Observation:

Load average was low.

Confirmed memory usage and CPU usage.

Identified PID of active processes.



###### 3\. Find specific process



Command:

'pgrep ssh'



Output:

Returned PID of ssh service.



Observation:

Confirms SSH service is active.



Service Checks (Using systemd)



Service inspected: ssh



###### 4\. Check service status



Command:

'systemctl status ssh'



Output:

Service is active (running).

Shows Main PID and uptime.



Observation:

Confirms service is healthy and enabled.



###### 5\. List running services



Command:

'systemctl list-units --type=service'



Observation:

Displays all active services currently running.

##### 

##### Log Checks



###### 6\. View service logs



Command:

'journalctl -u ssh -n 20'



Output:

Recent log entries related to SSH.



Observation:

Shows login attempts and service start messages.



###### 7\. View last 50 log lines



Command:

'tail -n 50 /var/log/syslog'



Observation:

System log entries including cron and authentication logs.

