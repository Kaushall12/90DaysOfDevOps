#### Linux User \& Group Management Challenge





##### 1\. Users \& Groups Created

Users Created



Commands used:



sudo useradd -m tokyo

sudo passwd tokyo



sudo useradd -m berlin

sudo passwd berlin



sudo useradd -m professor

sudo passwd professor



sudo useradd -m nairobi

sudo passwd nairobi



Verification:



cat /etc/passwd | grep tokyo

ls -l /home



Observation:

All users created with home directories under /home.



Groups Created



sudo groupadd developers

sudo groupadd admins

sudo groupadd project-team



Verification:



cat /etc/group | grep developers

cat /etc/group | grep admins



##### 2\. Group Assignments



Assign users to groups:



sudo usermod -aG developers tokyo



sudo usermod -aG developers berlin

sudo usermod -aG admins berlin



sudo usermod -aG admins professor



Add to project-team:



sudo usermod -aG project-team nairobi

sudo usermod -aG project-team tokyo



Verification:



groups tokyo

groups berlin

groups professor

groups nairobi



##### 3\. Shared Directory – Developers



Create directory:



sudo mkdir /opt/dev-project



Change group owner:



sudo chgrp developers /opt/dev-project



Set permissions:



sudo chmod 775 /opt/dev-project



Verify:



ls -ld /opt/dev-project



Test file creation:



sudo -u tokyo touch /opt/dev-project/test1.txt

sudo -u berlin touch /opt/dev-project/test2.txt



Observation:

Both users successfully created files.



##### 4\. Team Workspace – project-team



Create directory:



sudo mkdir /opt/team-workspace



Change group:



sudo chgrp project-team /opt/team-workspace



Set permissions:



sudo chmod 775 /opt/team-workspace



Verify:



ls -ld /opt/team-workspace



Test:



sudo -u nairobi touch /opt/team-workspace/teamfile.txt



Result:

File created successfully.



##### 5\. What I Learned



Users must belong to correct groups to access shared directories



Permissions 775 allow owner + group full access



Group ownership is critical in team environments



Always verify using ls -ld and groups



##### 6\. Real-World DevOps Use



Managing developers on shared servers



Restricting production access



Creating team-based deployment directories



Secure collaboration environments

