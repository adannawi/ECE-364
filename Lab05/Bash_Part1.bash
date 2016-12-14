#! /bin/bash

# $Author: ee364h10 $
# $Date: 2016-09-28 11:21:28 -0400 (Wed, 28 Sep 2016) $

function func_a 
{
    # Fill out your answer here.
    ls myDir/*.pdf | wc -l
    return
}

function func_b
{
    diff "foo1.txt" "foo2.txt" > help.txt
    flag=$?
    if (( flag==1 ))
    then
    echo "Files are different."
    else
    echo "Files are similar."
    fi
    return
}

function func_c 
{
    gcc -Wall -Werror "windows8.c" -o "windows8.o" 2>compile.out
    return
}

function func_d 
{
    # Fill out your answer here
    return 
}

function func_e
{
    string="abracadabra"
    echo ${string[0]}
    return
}

#
# To test your function, you can call it below like this:
#
#func_a
#func_b
func_c
#