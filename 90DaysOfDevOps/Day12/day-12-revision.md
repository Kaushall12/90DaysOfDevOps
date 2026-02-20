#### Revision \& Breather (Days 01–11)



##### 1\. Mindset \& Plan Check



Revisited my Day 01 learning plan.



Observations:



My goal of building strong Linux fundamentals still stands.



I’m getting more comfortable with troubleshooting flow.



I need to improve speed and command recall without checking notes.



Adjustment:

Focus next few days on speed + confidence, not just completion.



##### 2\. Processes \& Services Re-run



Commands re-tested:



ps aux | head



Observation:

Quick snapshot of running processes. Useful for confirming system activity.



systemctl status docker



Observation:

Service shows active (running). Confirms health and uptime.



journalctl -u docker -n 10



Observation:

Recent logs show daemon start messages. No critical errors.



Takeaway:

Always check status first, then logs.



##### 3\. File Skills Practice



Practiced:



echo "revision line" >> notes.txt

chmod 640 notes.txt

ls -l notes.txt



Observation:

Confirmed permission changes reflect immediately.



Also practiced:

sudo chown tokyo:developers devops-file.txt



Verified with:

ls -l devops-file.txt



Takeaway:

Ownership + permissions together control access.



##### 4\. Top 5 Commands I’d Use in an Incident



ps aux



top



systemctl status <service>



journalctl -u <service>



df -h



These give quick visibility into CPU, services, logs, and disk.



##### 5\. User/Group Sanity Check



Created test user:



sudo useradd -m testuser



Verified:



id testuser



Changed file ownership:



sudo chown testuser devops.txt



Verified:



ls -l devops.txt





Mini Self-Check
---



1\. Which 3 commands save you the most time?



systemctl status → instantly shows service health



journalctl -u → quick access to service logs



ps aux → fast process overview



They provide immediate visibility during incidents.





2\. How do you check if a service is healthy?



First commands I run:



systemctl status nginx

journalctl -u nginx -n 20

ss -tulpn | grep nginx



This checks service state, logs, and port listening.





3\. How do you safely change ownership \& permissions?



Example:



sudo chown tokyo:developers file.txt

sudo chmod 640 file.txt



Always verify with:

ls -l file.txt



Never blindly use chmod 777.





4\. Focus for Next 3 Days



Improve troubleshooting speed



Practice more real deployment scenarios



Start deeper Docker hands-on



Key Takeaway



Consistency matters more than complexity.

Small daily practice is building real confidence in Linux.

