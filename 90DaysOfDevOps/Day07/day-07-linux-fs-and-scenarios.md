#### Linux File System Hierarchy \& Scenario Practice





Part 1 – Linux File System Hierarchy

---

##### 1\. / (Root Directory)



Purpose:

The top-level directory. Everything in Linux starts from here.



Command:

ls -l /



Observed:

Directories like bin, etc, home, var, usr.



I would use this when I need to understand overall system structure.



##### 2\. /home



Purpose:

Contains personal directories for normal users.



Command:

ls -l /home



Observed:

User folders like kaushal.



I would use this when checking user files or scripts.



##### 3\. /root



Purpose:

Home directory for the root (administrator) user.



Command:

ls -l /root



Observed:

System-level configuration or admin files.



I would use this when performing privileged tasks.



##### 4\. /etc



Purpose:

Stores configuration files for services and the system.



Command:

ls -l /etc



Observed:

Files like hostname, hosts, ssh folder.



I would use this when editing service or system configuration.



##### 5\. /var/log



Purpose:

Contains system and service logs.



Command:

ls -l /var/log



Observed:

Files like syslog, auth.log, journal.



I would use this when troubleshooting errors.



##### 6\. /tmp



Purpose:

Temporary files. Often cleared after reboot.



Command:

ls -l /tmp



Observed:

Temporary runtime files.



I would use this when testing or storing short-term data.



Additional Directories

/bin



Purpose:

Essential system binaries (basic commands).



Example: ls, cp, mv



I would use this when verifying core commands exist.



/usr/bin



Purpose:

User-level command binaries.



Example: python, git



I would use this when checking installed applications.



/opt



Purpose:

Optional or third-party software.






Part 2 – Scenario-Based Practice


---

##### Scenario 1 – Service Not Starting





Step 1:

systemctl status myapp

Why: Check if service is failed or inactive.



Step 2:

journalctl -u myapp -n 50

Why: Review recent error logs.



Step 3:

systemctl is-enabled myapp

Why: Check if it starts on boot.



Step 4:

systemctl restart myapp

Why: Attempt controlled restart after reviewing logs.



What I learned: Always check logs before restarting.






##### 

##### Scenario 2 – High CPU Usage



Step 1:

top

Why: Identify processes consuming CPU in real-time.



Step 2:

ps aux --sort=-%cpu | head -10

Why: List top CPU-consuming processes.



Step 3:

pgrep process-name

Why: Confirm PID of suspected process.



Step 4:

kill -9 PID (if necessary)

Why: Stop runaway process carefully.




Scenario 3 – Finding Service Logs (docker)
---



Step 1:

systemctl status docker

Why: Confirm service state.



Step 2:

journalctl -u docker -n 50

Why: View recent logs.



Step 3:

journalctl -u docker -f

Why: Follow logs in real-time.



##### Scenario 4 – File Permission Issue



Step 1:

ls -l /home/user/backup.sh

Why: Check current permissions.



Step 2:

chmod +x /home/user/backup.sh

Why: Add execute permission.



Step 3:

ls -l /home/user/backup.sh

Why: Verify permission change.



Step 4:

./backup.sh

Why: Test script execution.

