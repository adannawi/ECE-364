#! /bin/bash

# $Author: ee364h10 $
# $Date: 2016-09-28 11:21:28 -0400 (Wed, 28 Sep 2016) $

if ((! $# ))
then
echo "Usage: ./assign_grades.bash <filename> <school>"
exit 1
fi

while read -a schools
do
  schoolName=$(echo ${schools[0]} | cut -c 1-2)
  courseNumber=$(echo ${schools[0]} | cut -c 3-5)
  studentNumber=$(echo ${schools[0]} | cut -c 6-8)
  letterGrade=$(get_letter_grade.bash ${schools[1]})
  echo $studentNumber, ${schools[1]}, $letterGrade >> students.db.$schoolName$courseNumber
done < $1

exit 0