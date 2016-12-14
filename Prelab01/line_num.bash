#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-08-26 15:51:00 -0400 (Fri, 26 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Prelab01/line_num.bash $
#$Revision: 91948 $

if (( !"$#" )) 
then
echo "Usage: line_num.bash <filename>"
else
    if [[ !(-r $1) ]]
    then
	echo "File $1 is unreadable!"
    else
	COUNTER=1
	while read line
	do
	   echo $COUNTER"."$line
	   let COUNTER=$COUNTER+1
	done < $1
    fi
fi