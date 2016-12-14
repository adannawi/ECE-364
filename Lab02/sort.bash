#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-09-07 10:57:05 -0400 (Wed, 07 Sep 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Lab02/sort.bash $
#$Revision: 93264 $

if (( !($#) ))
then
echo "Usage ./sort.bash <filename>"
exit 1
elif [[ !(-e $1) ]]
then
echo "$1 does not exist."
exit 2
else
    echo "The 5 fastest CPUs: "
    sort -k5 -n -t ',' $1 | head -n 5
    echo ""
    echo "The 3 most efficient CPUs: "
    sort -k4 -n -t ',' $1 | head -n 3
    echo ""
    echo "The CPUs with cache size 4: "
    sort -k5 -k2 -n -t ',' $1 >> sorted_$1
    
    while read Data
    do
     cacheSize=$(echo $Data | cut -d ',' -f2)
     if (( cacheSize==4 ))
     then
	 echo $Data
     fi
    done < sorted_$1

    if [[ -e sorted_$1 ]]
    then
       rm sorted_$1
    fi
    echo ""
    echo -n "Enter a value for n: "
    read input
    echo "The $input slowest CPUs: "
    sort -k5 -r -n -t ',' $1 | head -n $input
    sort -k1,1 -k4 -t ',' $1  > sorted_CPI.txt 
fi
