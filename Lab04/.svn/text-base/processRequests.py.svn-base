#! /usr/bin/env python3.4

def processRequests():
    userControls = getAccessControlByLogin()
    actionControl = getActionsOfController()
    processList = list()
    with open('ServerRequests.txt') as requestFile:
        all_lines = requestFile.readlines()
    for requestLine in all_lines:
        line = requestLine.split(" : ")
        userID = line[0].strip()
        webId = line[1].strip()
        specificLine = line[1].split("/")
        control = specificLine[3].strip()
        action = specificLine[4].strip()

        if (control in userControls[userID]):
           processTuple = (userID, webId, control, action, True)
        else:
           processTuple = (userID, webId, control, action, False)

        processList.append(processTuple)

    return processList
  # TODO: Remove the "pass" before you add any code to this block.


def getAccessControlByLogin():
    userControllers = {}
    controlSubset = set()
    with open('AccessControl.txt') as controlFile:
        all_lines = controlFile.readlines()
    for controlLine in all_lines[2:]:
        line = controlLine.split(":")
        #print(line)
        if (line[0].strip() in userControllers):
           # print(line[1].strip())
            userControllers[line[0].strip()].add(line[1].strip())
        else:
            userControllers[line[0].strip()] = {line[1].strip()}
    # TODO: Remove the "pass" before you add any code to this block.
    return userControllers


def getAccessControlByController():
    nameSet = set()
    nameDict = {}
    resultDict = {}
    uniqueController = {}

    with open('Logins.txt') as loginFile:
        all_lines = loginFile.readlines()
    for fileLine in all_lines[2:]:
        line = fileLine.strip().split("|")
        nameDict[line[1].strip()] = line[0].strip()

    with open('AccessControl.txt') as controlFile:
        all_lines2 = controlFile.readlines()
    for controlLine in all_lines2[2:]:
        line = controlLine.split(":")
        #print(line)
        if (line[1].strip() in uniqueController):
           # print(line[1].strip())
            uniqueController[line[1].strip()].add(line[0].strip())
        else:
            uniqueController[line[1].strip()] = {line[0].strip()}
    oneVal = 0
    for cont in uniqueController:
        for names in uniqueController[cont]:
          #  print(names)
            #if (names in resultDict):
          if (oneVal == 0):
           resultDict[cont] = {nameDict[names]}
           oneVal = 1
          else:
           resultDict[cont].add(nameDict[names])
        oneVal = 0
    return resultDict

    # TODO: Remove the "pass" before you add any code to this block.



def getActionsOfController():
    requestDict = {}
    with open('ServerRequests.txt') as requestFile:
        all_lines = requestFile.readlines()
    for requestLine in all_lines:
        line = requestLine.split(":")
        controlLine = line[2].split("/")
        control = controlLine[3].strip()
        action = controlLine[4].strip()
        if (control in requestDict):
            requestDict[control].add(action)
        else:
            requestDict[control] = {action}
    return requestDict
    # TODO: Remove the "pass" before you add any code to this block.


def isAccessAllowedFor(userID, url):
    userControls = getAccessControlByLogin()
    if (userID not in userControls):
        return False
    newURL = url.split("/")
    if (newURL[3] in userControls[userID]):
        return True
    return False
    # TODO: Remove the "pass" before you add any code to this block.


def getRequestsBy(userID):
    processList = processRequests()
    userLog = getAccessControlByLogin()
    tupleList = list()
    if (userID not in userLog):
        return tupleList

    for tuple in processList:
      if (tuple[0] == userID):
          access = isAccessAllowedFor(userID, tuple[1])
          newTuple = (tuple[1], access)
          tupleList.append(newTuple)
    tupleList.sort()
    return tupleList
    # TODO: Remove the "pass" before you add any code to this block.


def aggregateUserRequests():
    userList = getAccessControlByLogin()
    nameDict = {}
    accessDict = {}

    with open('Logins.txt') as loginFile:
        all_lines = loginFile.readlines()
    for fileLine in all_lines[2:]:
        line = fileLine.strip().split("|")
        nameDict[line[1].strip()] = line[0].strip()

    for name in userList:
        requests = getRequestsBy(name)
        numberRequests = len(requests)
        accessGranted = 0
        accessDenied = 0
        for request in requests:
          if (request[1] == True):
              accessGranted = accessGranted + 1
          else:
              accessDenied = accessDenied + 1
        accessDict[nameDict[name]] = (accessGranted, accessDenied)
    return accessDict
    # TODO: Remove the "pass" before you add any code to this block.


def aggregateControllerRequests():
    #Analyzes log file, returns a dict of te form {string:(int, int) where key is cont and value is a tuple
    #first element is number of URLS containing given cont granted access, second is denied access
    #userList = getAccessControlByLogin()
    urlGranted = 0
    urlDenied = 0
    aggregateDict = {}
    with open('ServerRequests.txt') as requestFile:
        all_lines = requestFile.readlines()
    for requestLine in all_lines:
        line = requestLine.split(":")
        name = line[0].strip()
        URL = "{0}:{1}".format(line[1], line[2]).strip()
        control = line[2].split("/")[3].strip()
        condition = isAccessAllowedFor(name, URL)
        if control not in aggregateDict:
            if condition is True:
                aggregateDict[control] = (urlGranted+1, urlDenied)
            else:
                aggregateDict[control] = (urlGranted, urlDenied+1)
        else:
            if condition is True:
                aggregateDict[control] = (aggregateDict[control][0]+1, aggregateDict[control][1])
            else:
                aggregateDict[control] = (aggregateDict[control][0], aggregateDict[control][1]+1)
    return aggregateDict
    # TODO: Remove the "pass" before you add any code to this block.


if __name__ == "__main__":
    #print(getAccessControlByLogin())
    #print(processRequests())
    #print(isAccessAllowedFor("jk4elly", "http://www.purdue.edu/Proceedings/Page14"))
    #print(getRequestsBy("jkelly"))
    #print(aggregateUserRequests())
    #print(getActionsOfController())
    print(aggregateControllerRequests())
    # TODO: Remove the "pass" before you add any code to this block.
    pass
