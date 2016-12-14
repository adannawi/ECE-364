#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-08-28 17:36:09 -0400 (Sun, 28 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Prelab01/sensor_sum.sh $
#$Revision: 92293 $

if (( !"$#" ))
then
    echo "usage: sensor_sum.sh log"
else
if [[ !(-e $1) ]]
then
    echo "$1 is not a readable file!"
else
#Good code
#Read command to extract columns
#Pipe echo to use cut
while read line
do
 id=$(echo $line | cut -d '-' -f1)
 numOne=$(echo $line | cut -f2 -'d ')
 numTwo=$(echo $line | cut -f3 -'d ')
 numThree=$(echo $line | cut -f4 -'d ')
 let sum=$numOne+$numTwo+$numThree
 echo $id $sum
done < $1
fi
fi

