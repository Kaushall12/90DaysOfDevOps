#### Shell Scripting: Functions \& Intermediate Concepts



##### Task 1 – Basic Functions



functions.sh



\#!/bin/bash



greet() {

&nbsp;   echo "Hello, $1!"

}



add() {

&nbsp;   local num1=$1

&nbsp;   local num2=$2

&nbsp;   echo "Sum: $((num1 + num2))"

}



greet "Kaushal"

add 5 10







#### Task 2 – Functions with System Checks



disk\_check.sh



\#!/bin/bash



check\_disk() {

&nbsp;   echo "Disk Usage:"

&nbsp;   df -h /

}



check\_memory() {

&nbsp;   echo "Memory Usage:"

&nbsp;   free -h

}



main() {

&nbsp;   check\_disk

&nbsp;   echo "---------------------"

&nbsp;   check\_memory

}



main





##### Task 3 – Strict Mode



strict\_demo.sh



\#!/bin/bash

set -euo pipefail



echo "Testing strict mode..."



\# Uncomment to test:

\# echo $UNDEFINED\_VAR



\# false



\# grep "hello" file.txt | wc -l







##### Task 4 – Local Variables



local\_demo.sh



\#!/bin/bash



test\_local() {

&nbsp;   local NAME="Kaushal"

&nbsp;   echo "Inside function: $NAME"

}



test\_global() {

&nbsp;   GLOBAL\_NAME="DevOps"

}



test\_local

echo "Outside function: ${NAME:-Not Defined}"



test\_global

echo "Global variable: $GLOBAL\_NAME"







##### Task 5 – System Info Reporter



system\_info.sh



\#!/bin/bash

set -euo pipefail



print\_header() {

&nbsp;   echo "=============================="

&nbsp;   echo "$1"

&nbsp;   echo "=============================="

}



system\_info() {

&nbsp;   print\_header "System Information"

&nbsp;   hostname

&nbsp;   uname -a

}



uptime\_info() {

&nbsp;   print\_header "Uptime"

&nbsp;   uptime

}



disk\_usage() {

&nbsp;   print\_header "Top Disk Usage"

&nbsp;   df -h | head -5

}



memory\_usage() {

&nbsp;   print\_header "Memory Usage"

&nbsp;   free -h

}



cpu\_usage() {

&nbsp;   print\_header "Top CPU Processes"

&nbsp;   ps aux --sort=-%cpu | head -6

}



main() {

&nbsp;   system\_info

&nbsp;   uptime\_info

&nbsp;   disk\_usage

&nbsp;   memory\_usage

&nbsp;   cpu\_usage

}



main





##### What I Learned



Functions make scripts modular and readable



local prevents variable conflicts



set -euo pipefail prevents silent failures



Real scripts should have a main function



Structure improves maintainability



