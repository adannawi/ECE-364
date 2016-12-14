import string
import re

def isIdValid(pin):
    for character in pin:
        if character in string.ascii_letters or character in string.digits or character == "_":
            pass
        else:
            return False
    return True

def parseAssignment(assignment):
    x = re.search(r"\.(.+)\((.+)\)", assignment)
    if x is None:
        raise ValueError(assignment)
    for item in x.groups():
        if isIdValid(item) is False:
            raise ValueError(assignment)
    return (x.group(1), x.group(2))


def parseLine(line):
    x = re.match(r"\s*(\S+)\s+(\S+)\s*\((.+)\)", line)
    if x is None:
        raise ValueError(line)
    if isIdValid(x.group(1).strip()) is False:
        raise ValueError(line)
    if isIdValid(x.group(2).strip()) is False:
        raise ValueError(line)
    pinList = []
    for item in x.group(3).strip().split(","):
        pinList.append(parseAssignment(item.strip()))
    return (x.group(1).strip(), x.group(2).strip(), tuple(pinList))

if __name__ == "__main__":
    #print(isIdValid("ABC_D012d"))
    #print(parseAssignment(".A(n32)"))
    #print(parseLine("  INVX4 U8 (.A(n2))"))
    print("yes!!")