#! /usr/bin/env python3.4

import re

def convertToAttrib():
    with open("points.xml") as pointFile:
        all_lines = pointFile.readlines()
        xmlString = "".join(all_lines)
    allIDs = re.findall(r"\s*<ID>\s*(.*)\s*</ID>\s*", xmlString)
    allXs = re.findall(r"\s*<X>\s*(.*)\s*</X>\s*", xmlString)
    allYs = re.findall(r"\s*<Y>\s*(.*)\s*</Y>\s*", xmlString)

    with open('points.out', 'w') as pointsOut:
        pointsOut.write('<?xml version="1.0"?>\n')
        pointsOut.write("<coordinates>\n")
        for i in range(0, len(allIDs)):
            returnString = '    <point ID="{0}" X="{1}" Y="{2}" />\n'.format(allIDs[i], allXs[i], allYs[i])
            pointsOut.write(returnString)
        pointsOut.write("</coordinates>")
def getGenres():
    with open("books.xml") as bookFile:
        all_lines = bookFile.readlines()
        bookString = "".join(all_lines)

    allGenres = list(set(re.findall(r"\s*<genre>\s*(.*)\s*</genre>\s*", bookString)))
    allGenres.sort()
    return(allGenres)
def getAuthorOf(bookName):
    with open("books.xml") as bookFile:
        all_lines = bookFile.readlines()
        bookString = "".join(all_lines)

    allAuthors = re.findall(r"\s*<author>\s*(.*)\s*</author>\s*", bookString)
    allTitles = re.findall(r"\s*<title>\s*(.*)\s*</title>\s*", bookString)

    if (bookName not in allTitles):
        return None

    authorDict = {}
    for i in range(0, len(allAuthors)):
        authorDict[allTitles[i]] = allAuthors[i]
    return(authorDict[bookName])
def getBookInfo(bookID):
    with open("books.xml") as bookFile:
        all_lines = bookFile.readlines()
        bookString = "".join(all_lines)

    allAuthors = re.findall(r"\s*<author>\s*(.*)\s*</author>\s*", bookString)
    allTitles = re.findall(r"\s*<title>\s*(.*)\s*</title>\s*", bookString)
    allBookID = re.findall(r'\s*<book id="(.*)">', bookString)

    if (bookID not in allBookID):
        return None

    tupleMania = {}
    for i in range(0, len(allBookID)):
        tupleMania[allBookID[i]] = (allTitles[i], allAuthors[i])

    return(tupleMania[bookID])

def getBooksBy(authorName):
    with open("books.xml") as bookFile:
        all_lines = bookFile.readlines()
        bookString = "".join(all_lines)

    allAuthors = re.findall(r"\s*<author>\s*(.*)\s*</author>\s*", bookString)
    allTitles = re.findall(r"\s*<title>\s*(.*)\s*</title>\s*", bookString)
    allBookID = re.findall(r'\s*<book id="(.*)">', bookString)

    if (authorName not in allAuthors):
        return None

    authorTuple = []
    bookList = []
    for i in range(0, len(allAuthors)):
        authorTuple.append((allAuthors[i], allTitles[i]))
    for ii in range(0, len(authorTuple)):
        if authorTuple[ii][0] == authorName:
            bookList.append(authorTuple[ii][1])
    return bookList

def getBooksBelow(bookPrice):
    with open("books.xml") as bookFile:
       all_lines = bookFile.readlines()
       bookString = "".join(all_lines)

    allTitles = re.findall(r"\s*<title>\s*(.*)\s*</title>\s*", bookString)
    allPrices = re.findall(r"\s*<price>\s*(.*)\s*</price>\s*", bookString)

    bookLessList = []
    for i in range(0, len(allTitles)):
        if float(allPrices[i]) < bookPrice:
            bookLessList.append(allTitles[i])
    bookLessList.sort()
    return bookLessList
def searchForWord(word):
    with open("books.xml") as bookFile:
       all_lines = bookFile.readlines()
       bookString = "".join(all_lines)

    allTitles = re.findall(r"\s*<title>\s*(.*)\s*</title>\s*", bookString)
    allDescriptions = re.findall(r"\s*<description>\s*(.*?)\s*</description>\s*", bookString, re.S)
    titleDescription = zip(allTitles, allDescriptions)
    matchList = []
    for title,description in zip(allTitles,allDescriptions):
      if re.search(r"\b(?:"+word+r")\b", description) is not None:
           print("Found a catch!")
           matchList.append(title)
      else:
         if re.search(r"\b(?:"+word+r")\b", title) is not None:
             print("Found a catch!")
             matchList.append(title)

    return matchList
if __name__ == '__main__':
    convertToAttrib()
    genreList = getGenres()
    print(getBooksBy("Kres, Peter"))
    #print(getBooksBelow(7))
    #print(searchForWord("C"))

