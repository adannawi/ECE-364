#! /usr/bin/env python3.4

def isValidOutput(fileName):
    with open(fileName) as sudokuFile:
        all_lines = sudokuFile.readlines()
    for sudList in all_lines:
        print(sudList)
    # TODO: Remove the "pass" before you add any code to this block.


def isColumnPuzzle(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def solvePuzzle(sourceFileName, targetFileName):

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def getCallersOf(phoneNumber):
    personNameList = []
    nameExt = {}
    with open ("People.txt") as peopleFile:
        all_lines = peopleFile.readlines()
    for peopleList in all_lines[2:]:
        formatPeople = peopleList.split("|")
        personName = formatPeople[0].strip()
        personExtension = formatPeople[1].strip()[1:]
        nameExt[personExtension] = personName
    with open ("ActivityList.txt") as activityFile:
        all_act = activityFile.readlines()
    for activityList in all_act[2:]:
        if activityList.split()[1] == phoneNumber:
            personNameList.append(nameExt[activityList.split()[0].split("-")[2]])
    personNameList.sort()
    return personNameList

def getCallActivity():

    nameExtension = {}
    activityDict = {}
    with open ("People.txt") as peopleFile:
        all_lines = peopleFile.readlines()
    for peopleList in all_lines[2:]:
        formatPeople = peopleList.split("|")
        personName = formatPeople[0].strip()
        personExtension = formatPeople[1].strip()[1:]
        nameExtension[personExtension] = personName
    extName = {ext:name for name,ext in nameExtension.items()}

    with open ("ActivityList.txt") as activityFile:
        all_act = activityFile.readlines()
    for perName, perExt in extName.items():
        callsMade = 0
        callTime = 0
        minutes = 0
        seconds = 0
        hours = 0
        for activityList in all_act[2:]:
            if activityList.split()[0].split("-")[2] == perExt:
                callsMade += 1
                #Calculate time here


                minutes += int(activityList.split()[2].split(":")[0])
                seconds += int(activityList.split()[2].split(":")[1])

                if seconds > 60:
                    minutes += 1
                    seconds -= 60
                if minutes > 60:
                    hours += 1
                    minutes -= 60

        callTime = "{0:02d}:{1:02d}:{2:02d}".format(hours, minutes, seconds)
        activityDict[perName] = (callsMade, callTime)
    return activityDict

if __name__ == "__main__":
    #getCallersOf("707-825-5871")
    getCallActivity()
    # TODO: Remove the "pass" before you add any code to this block.
    pass
