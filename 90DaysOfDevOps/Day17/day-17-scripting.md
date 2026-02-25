#### Shell Scripting: Loops, Arguments \& Error Handling





##### Task 1 – For Loop



for\_loop.sh





\#!/bin/bash



for fruit in apple banana mango orange grapes

do

&nbsp;   echo "Fruit: $fruit"

done





##### Task 2 – While Loop



countdown.sh



\#!/bin/bash



read -p "Enter a number: " NUM



while \[ $NUM -ge 0 ]

do

&nbsp;   echo $NUM

&nbsp;   NUM=$((NUM-1))

done



echo "Done!"





##### Task 3 – Command-Line Arguments



greet.sh



\#!/bin/bash



if \[ $# -eq 0 ]; then

&nbsp;   echo "Usage: ./greet.sh <name>"

&nbsp;   exit 1

fi



echo "Hello, $1!"





##### Task 4 – Install Packages via Script





install\_packages.sh



\#!/bin/bash



\# Check if running as root

if \[ "$EUID" -ne 0 ]; then

&nbsp;   echo "Please run as root"

&nbsp;   exit 1

fi



PACKAGES=(nginx curl wget)



for pkg in "${PACKAGES\[@]}"

do

&nbsp;   if dpkg -s "$pkg" \&> /dev/null; then

&nbsp;       echo "$pkg is already installed."

&nbsp;   else

&nbsp;       echo "Installing $pkg..."

&nbsp;       apt install -y "$pkg"

&nbsp;   fi

done





##### 

##### Task 5 – Error Handling





safe\_script.sh



\#!/bin/bash



set -e



mkdir /tmp/devops-test || echo "Directory already exists"



cd /tmp/devops-test || { echo "Failed to enter directory"; exit 1; }



touch test-file.txt || echo "Failed to create file"



echo "Script completed successfully."









##### What I Learned





for and while loops automate repetition



$1, $#, and $@ help handle script arguments



Always check if running as root when installing packages



set -e stops script on error



Exit codes and conditions make scripts safer

