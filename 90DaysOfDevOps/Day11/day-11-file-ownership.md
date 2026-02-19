#### File Ownership Challenge (chown \& chgrp)





##### 1\. Understanding Ownership



Command:



ls -l



Example output format:



-rw-r--r-- 1 kaushal kaushal 1200 Feb 16 devops.txt



Breakdown:



First column → permissions



Second → number of links



Third → owner (user)



Fourth → group



Then size, date, filename



Difference:



Owner → the user who controls the file



Group → set of users who share access rights



Owner has primary control. Group members get group-level permissions.



##### 2\. Basic chown Operations



Create file:



touch devops-file.txt



Check current owner:



ls -l devops-file.txt



Change owner to tokyo:



sudo chown tokyo devops-file.txt



Verify:



ls -l devops-file.txt



Change owner to berlin:



sudo chown berlin devops-file.txt



Verify again:



ls -l devops-file.txt



Observation:

Owner column changed successfully.



##### 3\. Basic chgrp Operations



Create file:



touch team-notes.txt



Check group:



ls -l team-notes.txt



Create group:



sudo groupadd heist-team



Change group:



sudo chgrp heist-team team-notes.txt



Verify:



ls -l team-notes.txt



Observation:

Group column updated.



##### 4\. Combined Owner \& Group Change



Create file:



touch project-config.yaml



Change owner and group in one command:



sudo chown professor:heist-team project-config.yaml



Verify:



ls -l project-config.yaml



Create directory:



mkdir app-logs



Change ownership:



sudo chown berlin:heist-team app-logs



Verify:



ls -ld app-logs



##### 5\. Recursive Ownership Change



Create structure:



mkdir -p heist-project/vault

mkdir -p heist-project/plans



touch heist-project/vault/gold.txt

touch heist-project/plans/strategy.conf



Create group:



sudo groupadd planners



Recursive change:



sudo chown -R professor:planners heist-project



Verify:



ls -lR heist-project



Observation:

All files and subdirectories now belong to professor:planners.



##### 6\. Practice Challenge – Mixed Ownership



Create directory:



mkdir bank-heist



Create files:



touch bank-heist/access-codes.txt

touch bank-heist/blueprints.pdf

touch bank-heist/escape-plan.txt



Create groups:



sudo groupadd vault-team

sudo groupadd tech-team



Set ownership:



sudo chown tokyo:vault-team bank-heist/access-codes.txt

sudo chown berlin:tech-team bank-heist/blueprints.pdf

sudo chown nairobi:vault-team bank-heist/escape-plan.txt



Verify:



ls -l bank-heist









##### Commands Used



ls -l

chown

chgrp

groupadd

useradd

mkdir

touch



##### 

##### 

##### What I Learned



Ownership controls access alongside permissions



chown can modify both user and group



-R flag changes ownership recursively



Users and groups must exist before assigning ownershi

