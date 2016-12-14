#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-08-26 15:51:00 -0400 (Fri, 26 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Prelab01/sum.bash $
#$Revision: 91948 $
SUM=0

while (( "$#" ))
do
 let SUM=$SUM+$1
 shift
done

 echo "Result is $SUM"