#### Shell Scripting Basics





##### Task 1 – Your First Script



hello.sh

\#!/bin/bash



echo "Hello, DevOps!"



Make executable:



chmod +x hello.sh

./hello.sh



Output:

Hello, DevOps!



What if shebang is removed?



If you remove:

\#!/bin/bash



The script may:



Still work if executed with bash hello.sh



Fail or behave differently if run as ./hello.sh



Use default shell instead of bash



Shebang tells the system which interpreter to use.







##### Task 2 – Variables



variables.sh

\#!/bin/bash



NAME="Kaushal"

ROLE="DevOps Engineer"



echo "Hello, I am $NAME and I am a $ROLE"





Single vs Double Quotes

echo '$NAME'



Prints literally: $NAME



echo "$NAME"





Single quotes → no variable expansion



Double quotes → variables are expanded





##### 

##### Task 3 – User Input





greet.sh



\#!/bin/bash



read -p "Enter your name: " NAME

read -p "Enter your favourite tool: " TOOL



echo "Hello $NAME, your favourite tool is $TOOL"







##### Task 4 – If-Else Conditions



check\_number.sh

\#!/bin/bash



read -p "Enter a number: " NUM



if \[ $NUM -gt 0 ]; then

&nbsp;   echo "Number is positive"

elif \[ $NUM -lt 0 ]; then

&nbsp;   echo "Number is negative"

else

&nbsp;   echo "Number is zero"

fi





##### 

##### Task 5 – Combine It All





server\_check.sh

\#!/bin/bash



SERVICE="ssh"



read -p "Do you want to check the status of $SERVICE? (y/n): " CHOICE



if \[ "$CHOICE" = "y" ]; then

&nbsp;   systemctl is-active --quiet $SERVICE

&nbsp;   if \[ $? -eq 0 ]; then

&nbsp;       echo "$SERVICE is active."

&nbsp;   else

&nbsp;       echo "$SERVICE is not active."

&nbsp;   fi

else

&nbsp;   echo "Skipped."

fi









##### What I Learned





Shebang defines interpreter



Variables need no spaces around =



Double quotes expand variables



if-else requires proper spacing inside \[ ]



Exit status ($?) helps check command success

