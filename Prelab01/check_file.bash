#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-08-26 18:10:01 -0400 (Fri, 26 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Prelab01/check_file.bash $
#$Revision: 91970 $

if (( !"$#" ))
then
echo "Usage: ./check_file.bash <filename>"
else
 if [[ -e $1 ]]
 then
 echo "$1 exists"
 else
 echo "$1 does not exist"
 fi
 if [[ -d $1 ]]
 then
 echo "$1 is a directory"
 else
 echo "$1 is not a directory"
 fi
 if [[ -f $1 ]]
 then
 echo "$1 is an ordinary file"
 else
 echo "$1 is not an ordinary file"
 fi
 if [[ -r $1 ]]
 then
 echo "$1 is readable"
 else
 echo "$1 is not readable"
 fi
 if [[ -w $1 ]]
 then
 echo "$1 is writable"
 else
 echo "$1 is not writable"
 fi
 if [[ -x $1 ]]
 then 
 echo "$1 is executable"
 else
 echo "$1 is not executable"
 fi
fi