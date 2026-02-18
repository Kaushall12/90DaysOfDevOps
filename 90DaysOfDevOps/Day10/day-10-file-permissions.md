#### File Permissions \& File Operations Challenge





##### 1\. Files Created

Create Files



touch devops.txt



echo "These are my DevOps notes" > notes.txt



vim script.sh



Inside script.sh:

echo "Hello DevOps"



Save and exit.



Verify:



ls -l



Observation:

Files created with default permissions (usually 644 for files).



##### 2\. Read Files



Read notes.txt:



cat notes.txt



View script.sh in read-only mode:



vim -R script.sh



View first 5 lines of passwd:



head -n 5 /etc/passwd



View last 5 lines:



tail -n 5 /etc/passwd



##### 3\. Understanding Permissions



Run:



ls -l devops.txt notes.txt script.sh



Example output:



-rw-r--r-- devops.txt

-rw-r--r-- notes.txt

-rw-r--r-- script.sh



Meaning:



Owner: read + write

Group: read

Others: read

No execute permission yet



Format:

rwxrwxrwx

Owner | Group | Others



Values:

r = 4

w = 2

x = 1



##### 4\. Modify Permissions

Make script executable



chmod +x script.sh



Verify:



ls -l script.sh



Now shows:

-rwxr-xr-x



Run:



./script.sh



Output:

Hello DevOps



Make devops.txt read-only



chmod a-w devops.txt



Verify:



ls -l devops.txt



Now no write permission.



Set notes.txt to 640



chmod 640 notes.txt



Meaning:

Owner: read + write

Group: read

Others: none



Verify:



ls -l notes.txt



Create directory with 755



mkdir project



chmod 755 project



Verify:



ls -ld project



Meaning:

Owner: full access

Group \& others: read + execute



##### 5\. Testing Permissions



Try writing to read-only file:



echo "test" >> devops.txt



Result:

Permission denied



Try executing file without execute permission:



Remove execute:



chmod -x script.sh



Run:



./script.sh



Result:

Permission denied



Commands Used



touch

echo

vim

cat

head

tail

chmod

ls



What I Learned



Default file permission is usually 644



Execute permission is required to run scripts



chmod can modify using symbolic (+x, -w) or numeric (755, 640)



Permission errors clearly indicate access problems

