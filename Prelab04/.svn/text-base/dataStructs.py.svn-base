import os

def uniqueLetters(s):
  letterList = []
  for character in s:
      if (character not in letterList or s.count(character) <= 1):
          letterList.append(character)

  letterList.sort()
  letterList.reverse()
  output = "".join(str(x) for x in letterList)
  return output

def scaleSet(aSet, num):
    a = []
    for value in aSet:
        tempScale = value*num
        a.append(round(tempScale,2))
    return set(a)

def printNames(aSet):
    nameList = list(aSet)
    nameList.sort()
    for name in nameList:
        print(name)

def getStateName(stateAbb):
    stateDict = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    for state, abbreviation in stateDict.items():
        if stateAbb == abbreviation:
            print(state)

def getZipCodes(stateName):
    d1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    d2 = {47906: "IN", 47907: "IN", 10001: "NY", 10025: "NY", 90001: "CA", 90005: "CA", 90009: "CA"}
    zipCodes = set()
    for state, abbreviation in d1.items():
        if state == stateName:
            toBeUsed = abbreviation
    for zipCode, abbreviation in d2.items():
        if abbreviation == toBeUsed:
            zipCodes.add(zipCode)
    return (zipCodes)

def printSortedMaps(s):
  oL = []
  for (lastName, firstName, mi), weight in s.items():
    o = "{1} {2} {0} has a weight of {3} lb.".format(lastName, firstName, mi, weight)
    oL.append(o)
  oL.sort()
  for string in oL:
    print(string)

def switchNames(s):
  nameString=""
  for (lastName, firstName, middleInit), weight in s.items():
    nameString = nameString+""+firstName+" "+lastName+" "
  return nameString

def getPossibleMatches(record, n):
  matchingNames = set()
  for name, (month, day, year) in record.items():
    if n == month or n == day or n == year:
        matchingNames.add(name)
  return matchingNames

def getPurchaseReport():
  pricingInfo = {}
  purchaseReports = {}
  if (os.path.exists('purchases/Item List.txt')):
    with open('purchases/Item List.txt', 'r') as priceFile:
        all_lines = priceFile.readlines()
    for line in all_lines[2::]:
        line = line.split()
        pricingInfo[line[0]] = line[1][1::]
  fileID = '000'
  while (os.path.exists('purchases/purchase_'+fileID+'.txt')):
    cost = 0
    with open('purchases/purchase_'+fileID+'.txt') as purchaseFile:
        all_lines = purchaseFile.readlines()
    for line in all_lines[2::]:
        line = line.split()
        cost = cost + (float(pricingInfo[line[0]]) * int(line[1]))
    purchaseReports[int(fileID)] = round(cost, 2)
    cost = 0
    fileID = '%03d' % (int(fileID) + 1)
  return purchaseReports

def getTotalSold():
  fileID = '000'
  totalSold = {"Grapes":10}
  while (os.path.exists('purchases/purchase_'+fileID+'.txt')):
    with open('purchases/purchase_'+fileID+'.txt') as purchaseFile:
        all_lines = purchaseFile.readlines()
    for line in all_lines[2::]:
        line = line.split()
        if line[0] in totalSold:
            totalSold[line[0]] = totalSold[line[0]] + int(line[1])
        else:
            totalSold[line[0]] = int(line[1])
    fileID = '%03d' % (int(fileID) + 1)
  print(totalSold)

if __name__ == "__main__":
  testList = uniqueLetters("ABDBDARWET")
  setToTest = {3.12, 5.0, 7.2, 15.24}
  nameSet = {"John", "Abraham", "Cassandra", "Wukong"}
  scaleValue = 2.1
  scaledSet = scaleSet(setToTest, scaleValue)
  s = {("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9}
  record = {"Mister Bean":(9, 5, 90), "Frank Xavier":(12, 5, 95), "Jamuel Sackson":(1, 9, 84)}
  #printNames(nameSet)
  #getStateName("IN")
  resultZip = getZipCodes("California")
  nameKey = switchNames(s)
  nameMatchSet =getPossibleMatches(record,95)
  report = getPurchaseReport()
  getTotalSold()
