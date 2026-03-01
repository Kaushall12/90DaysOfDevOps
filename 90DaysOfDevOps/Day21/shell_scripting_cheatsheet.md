#### Shell Scripting Cheat Sheet



##### 

##### 1\. Basics



Shebang



\#!/bin/bash



Specifies interpreter. Required for executable scripts.



Running a Script



chmod +x script.sh

./script.sh

bash script.sh



Comments



\# Single line comment

echo "Hello"  # Inline comment



Variables



NAME="Kaushal"

echo $NAME

echo "$NAME"

echo '$NAME'



Double quotes expand variables



Single quotes don’t





User Input



read -p "Enter name: " NAME



Arguments



$0 → script name

$1 → first argument

$# → argument count

$@ → all arguments

$? → last command exit code







##### 2\. Operators \& Conditionals



String Comparison



\[ "$A" = "$B" ]

\[ -z "$VAR" ]   # empty

\[ -n "$VAR" ]   # not empty



Integer Comparison



\[ $A -eq $B ]

\[ $A -gt 10 ]



File Tests



\[ -f file ]  # file exists

\[ -d dir ]   # directory exists

\[ -r file ]  # readable

\[ -x file ]  # executable



If Syntax



if \[ condition ]; then

&nbsp;   echo "Yes"

elif \[ other ]; then

&nbsp;   echo "Maybe"

else

&nbsp;   echo "No"

fi



Logical Operators



command \&\& echo "Success"

command || echo "Failed"

! command



Case Statement



case $VAR in

&nbsp;   start) echo "Starting";;

&nbsp;   stop) echo "Stopping";;

&nbsp;   \*) echo "Unknown";;

esac





##### 3\. Loops



For Loop



for i in 1 2 3; do

&nbsp;   echo $i

done



C-style:



for ((i=1;i<=5;i++)); do

&nbsp;   echo $i

done



While Loop



while \[ $NUM -gt 0 ]; do

&nbsp;   echo $NUM

&nbsp;   NUM=$((NUM-1))

done



Until Loop



until \[ $NUM -eq 0 ]; do

&nbsp;   echo $NUM

done



Loop Over Files



for file in \*.log; do

&nbsp;   echo $file

done



Loop Over Command Output



ls | while read line; do

&nbsp;   echo $line

done



##### 4\. Functions



Define \& Call



greet() {

&nbsp;   echo "Hello $1"

}



greet "Kaushal"



Return vs Echo



return 0  # exit status

echo "Value"  # actual output



Local Variables



myfunc() {

&nbsp;   local NAME="DevOps"

}





##### 5\. Text Processing Commands





grep



grep -i "error" log.txt

grep -r "pattern" .

grep -c "error" log.txt



awk



awk '{print $1}' file

awk -F: '{print $1}' /etc/passwd



sed



sed 's/old/new/g' file

sed -i 's/foo/bar/g' file



cut



cut -d: -f1 /etc/passwd

sort \& uniq

sort file.txt

sort -nr numbers.txt

uniq -c file.txt



tr



tr 'a-z' 'A-Z'



wc



wc -l file.txt

wc -w file.txt



head / tail



head -n 5 file.txt

tail -n 10 file.txt

tail -f logfile.log



##### 6\. Useful One-Liners



Delete files older than 7 days:



find . -type f -mtime +7 -delete



Count lines in all .log files:



wc -l \*.log



Replace text in multiple files:



sed -i 's/old/new/g' \*.txt



Check if service is running:



systemctl is-active nginx



Monitor disk usage:



df -h | grep -v tmpfs



Tail logs and filter errors:



tail -f app.log | grep ERROR





##### 7\. Error Handling \& Debugging



Exit Codes



exit 0  # success

exit 1  # failure

echo $? # check last status



Strict Mode



set -e

set -u

set -o pipefail

set -x  # debug mode



Trap



trap 'echo "Exiting..."; cleanup' EXIT







##### What I Learned





Structure matters more than syntax



Strict mode prevents silent failures



grep + awk + sed are extremely powerful



Functions improve readability



One-liners save time in real incidents

