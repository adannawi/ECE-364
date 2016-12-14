#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-08-31 11:02:12 -0400 (Wed, 31 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Lab01/mini_shell.bash $
#$Revision: 92788 $
flag=0
while ((!$flag))
do

echo -n "Enter a command: "
read input </dev/tty

if [[ "$input" = "quit" ]]
then
flag=1
echo Goodbye
elif [[ "$input" = "hello" ]]
then
echo "Hello $USER"
elif [[ "$input" = "compile" ]]
then
for File in *.c
do
cutFile=$(echo $File | cut -d '.' -f1) 
gcc -Wall -Werror "$File" -o "$cutFile.o"
if [[ "$?" = "0" ]]
then
echo "Compilation succeeded for: $File"
elif [[ "$?" = "1" ]]
then
echo "Compilation failed for: $File"
fi
done
elif [[ "$input" = "run" ]]
then
    echo -n "Enter a filename: "
    read filename </dev/tty
    echo -n "Enter arguments: "
    read arguments </dev/tty
  if [[ !(-x $filename && -r $filename) ]]
   then
    echo "Invalid filename"
  else
    ./$filename $arguments
  fi
else
 echo "Error: unrecognized input"
fi
done
