#### Revision (Days 1–27)



##### 1\. Self-Assessment



Linux



-> Navigate the file system, create/move/delete files and directories  

-> Manage processes using ps, top, kill  

-> Manage services with systemctl  

-> Work with text files using cat, head, tail, vim  

-> Troubleshoot CPU, memory, and disk usage using top, free, df, du  

-> Understand Linux file system hierarchy (/etc, /var, /home, /tmp)  

-> Create users and groups  

-> Set file permissions with chmod  

-> Change ownership with chown and chgrp  

-> Understand LVM basics  

-> Check networking with ping, curl, ss, dig  



---



Shell Scripting



-> Write scripts using variables and arguments  

-> Use if/else conditions  

-> Write for and while loops  

-> Define functions and pass arguments  

-> Use grep, awk, sed for text processing  

-> Handle errors with set -euo pipefail  

-> Schedule scripts using crontab  



---



Git \& GitHub



-> Initialize repositories and commit changes  

-> Work with branches  

-> Push and pull from GitHub  

-> Understand clone vs fork  

-> Merge branches and understand fast-forward merge  

-> Use rebase to maintain clean history  

-> Use git stash to save temporary work  

-> Cherry-pick commits between branches  

-> Understand squash merge vs normal merge  

-> Use git reset and git revert  

-> Understand GitFlow, GitHub Flow, Trunk-Based Development  

-> Use GitHub CLI for repo and PR management  



---



##### 2. Topics Revisited



Topic 1: LVM



Revisited how physical volumes, volume groups, and logical volumes work together to manage storage flexibly.



Topic 2: Git Rebase



Relearned how rebase rewrites commit history by replaying commits on top of another branch.



Topic 3: Shell Error Handling



Practiced using set -euo pipefail to prevent scripts from silently failing.



---



##### 3\. Quick-Fire Questions



What does chmod 755 script.sh do?



It gives the owner full permissions (read, write, execute) and gives group and others read and execute permissions.



---



Difference between a process and a service?



A process is a running program in memory.  

A service is a background process managed by the system (often via systemd).



---



How to find which process is using port 8080?



