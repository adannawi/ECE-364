#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-09-02 13:24:46 -0400 (Fri, 02 Sep 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Prelab02/process_temps.bash $
#$Revision: 92844 $
if (( !$# ))
then
 echo "Usage process_temps.bash <input file>"
 exit 1
else
 if [[ !(-r $1) ]]
 then
  echo "$1 is not a readable file."
 else
  sed 1d $1 | while read -a Data
  do
    TotalTemp=0
    currTime=${Data[0]}
    tempArr=("${Data[@]:1}")
    tempSize=${#tempArr[*]}
    for temperature in ${tempArr[*]};
    do
        let TotalTemp=$TotalTemp+$temperature
    done
    let averageTemp=$TotalTemp/$tempSize
    echo "Average temperature for time $currTime was $averageTemp C."
  done
 fi
fi
