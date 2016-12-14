#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-09-01 14:23:13 -0400 (Thu, 01 Sep 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Prelab02/run.bash $
#$Revision: 92831 $
if ((!($#==2)))
then
    echo "usage: run.bash <filename> <output_filename>"
else
gcc $1 -o quick_sim
if (($?==1))
then
    echo "error: quick_sim could not be compiled!"
    exit 1
else
   fileToUse=$2
   fastestSpeed=0
   fastestBrand=0
   fastestSize=0
   fastestWidth=0
   #Check if file exists, then prompt user to delete if it does, or to rename if they decline.
   if [ -e $2 ]
   then
    echo -n "$2 exists. Would you like to delete it? "
    read input
    if [[ $input == "y" || $input == "yes" ]]
    then
     rm $2
    else
     echo -n "Enter a new filename: "
     read newName
     fileToUse=$newName
    fi   
   fi
   for J in 1 2 4 8 16 32
   do
    for K in 1 2 4 8 16
    do
     for I in a i
      do
    result=$(quick_sim $J $K $I)
    #echo $result >> $fileToUse
    #Crunch results and extract cache size, issue width, CPI, and execution time
    cacheSize=$(echo $result | grep -o 'size:[^ ,]\+'  | cut -d ':' -f2)
    issueWidth=$(echo $result | grep -o 'width:[^ ,]\+' | cut -d ':' -f2)
    CPI=$(echo $result | grep -o 'CPI:[^ ,]\+' | cut -d ':' -f2)
    execTime=$(echo $result | grep -o 'time:[^ ,]\+' | cut -d ':' -f2)
    if [[ $I == "a" ]]
      then
       brand="AMD Opteron"
      elif [[ $I == "i" ]]
      then
       brand="Intel Core i7"
      fi
    output=$brand:$cacheSize:$issueWidth:$CPI:$execTime
    echo $output >> $fileToUse
    if [[ $execTime > $fastestTime ]]
    then
      fastestSpeed=$execTime
      fastestBrand=$brand
      fastestSize=$cacheSize
      fastestWidth=$issueWidth
      fi
    done
   done
  done
  echo Fastest run time achieved by $fastestBrand with a cache size $fastestSize and a issue width $fastestWidth was $fastestSpeed
fi
fi