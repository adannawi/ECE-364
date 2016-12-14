#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-08-26 15:18:19 -0400 (Fri, 26 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Prelab01/exist.bash $
#$Revision: 91944 $

#List of files, if readable, print readable, otherwise create empty file /w name
while (( "$#" ))
do
 if [[ !(-r $1) ]]
     then
     touch $1
     else
     echo "File $1 is readable!"
     fi
shift
done