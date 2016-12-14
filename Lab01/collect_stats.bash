#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-08-31 09:56:35 -0400 (Wed, 31 Aug 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Lab01/collect_stats.bash $
#$Revision: 92745 $
if (( !($#==2) ))
then
 echo "Usage: ./collect_stats.bash <file> <sport>"
 exit 1
else
if [[ !(-e $1) ]]
then
 echo "Error: $1 does not exist"
 exit 2
else
 numAthletes=0
 numMedals=0
 maxMedals=0
 while read line
do
 name=$(echo $line | cut -d ',' -f1)
 sport=$(echo $line | cut -d ',' -f2)
 medals=$(echo $line | cut -d ',' -f3)

 if [[ ("$sport" = "$2") ]]
 then
 ((numAthletes=$numAthletes+1))
 ((numMedals=$numMedals+$medals))
 if (( $medals>$maxMedals ))
 then
  ((maxMedals=$medals))
  winnerName=$name
 fi
 fi
done < $1
 echo "Total athletes: $numAthletes"
 echo "Total medals won: $numMedals"
 echo "$winnerName won the most medals: $maxMedals"
 exit 0
fi
fi
