#### Linux Troubleshooting Runbook





##### 1\. Environment Basics

Command:



'uname -a'



Observation:

Confirmed kernel version and architecture (Linux x86\_64).



Command:



'cat /etc/os-release'



Observation:

System is running Ubuntu 22.04 LTS.



##### 2\. Filesystem Sanity Check

Command:



'mkdir /tmp/runbook-demo'



Command:



'cp /etc/hosts /tmp/runbook-demo/hosts-copy \&\& ls -l /tmp/runbook-demo'



Observation:

Directory and file created successfully. Filesystem is writable and permissions are correct.



##### 3\. CPU \& Memory Snapshot

Command:



'top'



Observation:

Load average below 1.0. CPU mostly idle. No abnormal spikes.



Command:



'free -h'



Observation:

Sufficient available memory. No swap pressure observed.



Command:



'ps -o pid,pcpu,pmem,comm -p $(pgrep ssh)'



Observation:

SSH process consuming minimal CPU and memory.



##### 4\. Disk \& IO Snapshot

Command:



'df -h'



Observation:

Root partition below 60% usage. No disk saturation.



Command:



'du -sh /var/log'



Observation:

Log directory size normal. No unexpected growth.



##### 5\. Network Snapshot

Command:



'ss -tulpn | grep ssh'



Observation:

SSH listening on port 22. Service bound to correct interface.



Command:



'curl -I http://localhost

'



Observation:

Local web endpoint responding with HTTP status 200 (if applicable).



##### 6\. Logs Reviewed

Command:



'journalctl -u ssh -n 50'



Observation:

No recent errors. Only successful login entries.



Command:



'tail -n 50 /var/log/auth.log'



Observation:

Authentication logs normal. No repeated failed attempts.



##### 7\. Quick Findings



SSH service is running and healthy



CPU, memory, and disk usage are stable



No critical errors in logs



Network port is listening correctly



System operating normally.





