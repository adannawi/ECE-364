from points import PointND
from prelab08addon import performProcessing

def createPoint(dataString):
    floatList = []
    try:
        commaList = dataString.split(",")
        for entry in commaList:
          entry.strip()
          floatList.append(float(entry))
        print(floatList)
        newPoint = PointND(*floatList[0:len(commaList)])
        return newPoint
    except:
        return "nope"

def distanceBetween(point1, point2):
    try:
        distance = point1.distanceFrom(point2)
    except:
        distance = "Something went wrong!"
    return distance

def checkVicinity(point, pointList, radius):
    closePoint = 0
    farPoint = 0
    invalidPoint = 0
    for somePoint in pointList:
        try:
            if (distanceBetween(point, somePoint) > radius):
                farPoint += 1
            elif (distanceBetween(point, somePoint) < radius):
                closePoint += 1
        except:
            invalidPoint += 1
    return (closePoint, farPoint, invalidPoint)

def checkOperation(*args):
    try:
        performProcessing(*args)
        return True
    except BlockingIOError as err:
        return "The following Error occurred: {0}".format(type(err))
    except TypeError as err:
        return "The following Error occured: {0}".format(type(err))
    except ValueError as err:
        return "The following Error occured: {0}".format(type(err))
    except OSError as err:
        return "The following Error occured: {0}".format(type(err))
    except IndexError as err:
        return "The following Error occured: {0}".format(type(err))
    except KeyError as err:
        return "The following Error occured: {0}".format(type(err))
    except ConnectionRefusedError:
        raise ConnectionRefusedError("Connection refused.")
    except:
        return False

if __name__ == "__main__":
    newP = PointND(5.0, 3.0, 2.0)
    otherP = PointND(6.0, 1.0, 2.0, 5.0)
    point1 = PointND(1.0, 2.0, 3.0)
    point2 = PointND(5.0, 4.0, 2.5)
    point3 = PointND(3.0, 2.0, 5.0)
    point4 = PointND(1.0, 2.0, 3.0, 4.0)
    pointZero = PointND(0.0, 0.0, 0.0)
    pointList = [point1, point2, point3, point4]
    splitComma = "4.3,2.1,1.5,5"
    splitComma2 = "4.3, 3FA2, None"
    newP3 = createPoint(splitComma)
    print(newP3)
   # print(distanceBetween(newP, otherP))
    #print(checkVicinity(pointZero, pointList, 6.0))
    #print(checkOperation("Hi"))