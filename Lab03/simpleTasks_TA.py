

# The following variable(s) are the only lines of code that should be outside of a function.

accounts = [
    'Mark Thomas:    $11.99   $52.08   $81.15   $79.16   $16.23   $88.11   $21.20   $0.02   ',
    'Gregory Powell:      $97.42     $96.05     $71.82     $24.79     $14.42     $60.84     $35.46     ',
    'Kevin Wood:     $93.37    $16.73    $97.05    $14.57    $53.29    ',
    'Martin Watson:     $20.53    $90.58    $22.07    $1.28    $75.40    $48.98    $36.46    $42.65    $5.01  $52.62  ',
    'Frank Young:     $32.02    $51.20    $0.99    $51.85    $88.38    $67.26    $62.72    $47.36    $38.89    ',
    'Michelle Thompson:     $2.44    $100.72    $81.44    $48.07    $68.71    $23.11    $79.23    $71.02    ',
    'Anne Harris:     $30.10    $58.32    $6.22    $3.67    $30.02    $37.65    $6.17    $41.30    $51.15    ',
    'Kelly Cooper:      $73.74     $57.63     $91.94     $42.94     $59.26     $64.30     $13.59     $19.69     $4.11 ',
    'Benjamin Foster:      $4.22     $63.02     $73.07     $99.73     $24.00     $77.79     $20.30     ',
    'Marie Perry:    $32.90   $80.27   $70.18   $68.74   $14.11   $7.38   ',
    'Cynthia Simmons:      $91.64     $56.95     $40.73     $61.28     $53.88     $77.05     $6.88     $23.37     ']

test = ["George Teal:   $1.00   $2.00   $3.00   $4.01   ",
        "Christine Doyle:   $10.51  $22.49  $12.00  $5.33   $100.00 "]


def getRowSum(accList):
    rowSum = []

    for item in accList:
        elements = item.split()[2:].replace("$", "")
        total = sum([float(i) for i in elements])
        rowSum.append(round(total, 2))

    return rowSum

def getDoublePalindromes():

    paliList = []
    # TODO: Remove the "pass" before you add any code to this block.
    for i in range(10, 1000000):
        binI = bin(i)
        binI = binI[2:]
        if ((str(i)[::-1] == str(i)) and (str(binI)[::-1] == str(binI))):
            paliList.append(i)
    return paliList

def scaleVector(s, vList):

    return [s*i for i in vList]

def convertToBoolean(num):

    if num not in range(0, 255) or type(num) is not int:
        return None

    binNum = "{0:08b}".format(num)
    boolList = [True if i == "1" else False for i in binNum]

    return boolList

def convertToInteger(boolList):

    if type(boolList) is not list or len(boolList) == 0:
            return None

    strList = "".join(["1" if i else "0" for i in boolList])
    integerVal = int(strList, 2)

    return integerVal

def getWords(sentence, n):

    sentence = "hello world it is monday"
    uniqueList = []
    uniqueSentence = removeDuplicates(sentence.split())

    for word in uniqueSentence:
        if len(word) == n:
            uniqueList.append(word)
    return uniqueList

def removeDuplicates(l):
    target = []
    for i in l:
        if i not in target:
            target.append(i)
    return target
def isSubListOf(superList, subList):
    for i in range(len(superList)-len(subList)+1):
        if subList == superList[i:i+len(subList)]:
            return True
    return False
def getElementsAt(l, i):

    # TODO: Remove the "pass" before you add any code to this block.
    pass


if __name__ == "__main__":
    test = getRowSum(test)
    palilist = getDoublePalindromes()
    list2 = [0, 1, 8, 3]
    smallList = [8, 2] #false
    smallList2 = [-3, 2, 2, 8]#true
    smallList3 = [0, -3, 8]#false
    bigList = [0, -3, 2, 2, 8, 1, 4]
    joke = scaleVector(3.14, list2)
    boolList2 = convertToBoolean(135)
    boolList3 = convertToInteger(boolList2)
    wordList = getWords("the power of this engine matches that of the one we use last year", 5)
    isSubSet1 = isSubListOf(bigList, smallList)
    isSubSet2 = isSubListOf(bigList, smallList2)
    isSubSet3 = isSubListOf(bigList, smallList3)

    print (isSubSet1)
    print (isSubSet2)
    print (isSubSet3)
