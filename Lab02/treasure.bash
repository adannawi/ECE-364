#! /bin/bash
#
#$Author: ee364h10 $
#$Date: 2016-09-09 15:52:16 -0400 (Fri, 09 Sep 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364h10/Lab02/treasure.bash $
#$Revision: 93323 $
if (( !($#) ))
then
echo "Usage: ./treasure.bash <filename>"
exit 1
elif [[ !(-e $1) ]]
then
echo "$1 does not exist."
else
isDone=0
mapArray=()
numRows=0
while read -a map
do
for value in ${map[@]};do
mapArray+=($value)
done
let numRows=$numRows+1
done < $1
echo there are $numRows rows.

xCoord=0
yCoord=0
while (( !isDone )); do
    echo "($xCoord, $yCoord)"
    #Check where we go next
    let newIndex=($numRows*$xCoord)+$yCoord #02 should go to index 2
    #Check content of that index
    toBeChecked=${mapArray[$newIndex]}
    #Cut result [XY] into coordinates.
    newX=$(echo $toBeChecked | cut -c 1)
    newY=$(echo $toBeChecked | cut -c 2)
    #Now that we have the clues to the next location
    #We should check if this is the treasure first
    if (( $xCoord==$newX && $yCoord==$newY ))
    then
    echo "Treasure found at ($xCoord, $yCoord)."
    isDone=1
    fi
    #If it isn't found, we should move on.
    xCoord=$newX
    yCoord=$newY
done
fi
# 0 1 2     0 1 2 3 4 5 6 7 8 #SizeofRow*Y + X
# a b c 0 | a b c d e f g h i
# d e f 1
# g h i 2