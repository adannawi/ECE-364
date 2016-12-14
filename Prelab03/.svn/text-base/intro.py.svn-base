#! /usr/bin/evn python3.4

import os
import sys
import math

def getHeadAverage(l, n):
  avg = sum(l[:n])/n
  return avg

def getTailMax(l, m):
  l.reverse()
  maxNum = max(l[:m])
  return maxNum

def getNumberAverage(l):
  new_list = []
  for value in l:
      if type(value) is int:
          new_list.append(value)
  listSize = len(new_list)
  avg = sum(new_list)/listSize
  return avg

def getFormattedSSN(n):
    length=len(str(n))
    newSSN = str(n)
    if (length < 9):
        amountToAdd=9-length

        while(amountToAdd > 0):
            newSSN = "0"+newSSN
            amountToAdd -= 1
    formattedSSN = newSSN[0:3]+"-"+newSSN[3:5]+"-"+newSSN[5:]
    return formattedSSN

def findName(l, s):
  for name in l:
      newName = name.split()
      for firstLast in newName:
       if (firstLast == s):
         resultingName = newName
         return " ".join(resultingName)

  return "not found"

def getColumnSum(mat):
  sumList = []
  sum = 0
  for row in range(0,len(mat[0])):
    for column in range(0,len(mat)):
        sum += mat[column][row]
    sumList.append(sum)
    sum = 0

  return sumList

def getFormattedNames(ln):
  fixedNames = []
  for fullName in range(0, len(ln)):
      tempName = ln[fullName][2]+", "+ln[fullName][0]+" "+ln[fullName][1]+"."
      fixedNames.append(tempName)
  return fixedNames

def getElementwiseSum(l1, l2):
  elementWise = []
  diffInLength = abs(len(l2)-len(l1))
  lengthToAdd = max(len(l1), len(l2))
  flag = 0
  for i in range(0, diffInLength):
    if (len(l1) > len(l2)):
      l2.append(0)
      flag = 1
    elif (len(l1) < len(l2)):
      l1.append(0)
      flag = 2

  for i in range(0, lengthToAdd):
    sum = l1[i]+l2[i]
    elementWise.append(sum)

  return elementWise

def removeDuplicates(l):
    newList = l
    for i in newList:
      if (newList.count(i)>1):
          for j in range(0, newList.count(i)-1):
            newList.remove(i)
    return newList

def getMaxOccurrence(l):
    newList = l
    maxElement = 0
    maxCount = 0
    for i in newList:
        if (newList.count(i)>1):
          if (newList.count(i)>maxCount):
              maxCount = newList.count(i)
              maxElement = newList[i+1]
    return maxElement

def getMaxProduct(l):
    length = len(l)
    maxProduct = 0
    for i in range(0, length):
        if (i+2 < length):
            product = l[i]*l[i+1]*l[i+2]
        if (maxProduct < product):
            maxProduct = product
    return maxProduct

#Entry point
if __name__ == "__main__":
  list = [4, 20, 3, 2, 1, 9, 10]
  multilist = [4, "hello", 5, "jemimah", True, False, 3, 8]
  listNames = ["Dwayne Johnson", "John Cena", "Donald Trump", "Test Bobby", "Bobby Jackson"]
  list2 = ["Geoge Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
  targetName = "Bobby"
  mat = []
  mat1 = [1, 2, 3, 5, 1]
  mat2 = [2, 3, 4, 5, 2]
  mat3 = [5, 6, 7, 5, 3] #210
  mat4 = [1, 1, 1, 1, 4]
  mat.append(mat1)
  mat.append(mat2)
  mat.append(mat3)
  mat.append(mat4)
  amount = 6
  SSN=1657649
  nameList = [["George", "W", "Bush"], ["Dwayne", "J", "Johnson"]]
  addList1 = [1, 3, 5, 7, 9, 11]
  addList2 = [6, 4, 2]
  dupeList = [1, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6]
  l1 = [1, 1,1, 1, 1,1 ,1,1 ,1, 3, 2, 2, 7, 9, 2, 2, 11, 2]
  l3 = [3, 7, -2, 2, 3, 5]
  avg = getHeadAverage(list, amount)
  maxNum = getTailMax(list, amount)
  multiAvg = getNumberAverage(multilist)
  formatSSN = getFormattedSSN(SSN)
  firstName = findName(listNames, targetName)
  sumColumn = getColumnSum(mat)
  formatList = getFormattedNames(nameList)
  elementSum = getElementwiseSum(addList1, addList2)
  cleanList = removeDuplicates(dupeList)
  maxOccurence = getMaxOccurrence(l1)
  maxProduct = getMaxProduct(mat2)
  print maxProduct

