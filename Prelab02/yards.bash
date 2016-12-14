#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-09-03 12:14:47 -0400 (Sat, 03 Sep 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Prelab02/yards.bash $
#$Revision: 92873 $
if (( !"$#" ))
then
echo "Usage: yards.bash <filename>"
else
if
 [[ -r $1 ]]
then
 #readable, good stuff
#Read file
#Get line
#Do things to line (save name, do thingsto yards, get average, store if bigger)
  HighestAverage=0
  while read -a Data
  do
      numberOfEntries=${#Data[*]}
      ((numberOfCalcEntries=$numberOfEntries-1))
      indexList=${!Data[*]}
      nameOfSchool=${Data[0]}
      runningTotal=0

      for i in ${Data[*]:1}
      do
      ((runningTotal=$runningTotal+$i))
      done

      ((Average=$runningTotal/$numberOfCalcEntries))

      for i in ${Data[*]:1}
      do
       ((Subtotal=$Subtotal+(($i-$Average))**2))
      done

      ((Variance=$Subtotal/$numberOfCalcEntries))

      echo $nameOfSchool schools averaged $Average yards receiving with a variance of $Variance
      Subtotal=0
      if (($Average>$HighestAverage))
      then
	  HighestAverage=$Average
      fi
  done < $1
  echo The largest average yardage was $HighestAverage
else
echo "Error: $1 is not readable"
fi
fi