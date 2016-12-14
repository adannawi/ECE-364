import math

class PointND:
    def __init__(self, *args):
        for arg in args:
            if type(arg) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")
        self.t = args
        self.n = len(self.t)

    def __str__(self):
        formatStr = ""
        for item in self.t:
            formatStr += format(item, '.2f')
            formatStr += ", "
        formatStr = formatStr.strip()
        formatStr = formatStr.strip(",")
        return "("+formatStr+")"

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if self.n != other.n:
            raise ValueError("Cannot calculate distance between two points of different cardinality.")
        sum=0
        for pointX,pointY in zip(self.t,other.t):
            sum+=pow((pointX-pointY),2)
        distance = math.sqrt(sum)
        return distance

    def nearestPoint(self, points):
        if (len(points) == 0):
            raise ValueError("Input cannot be empty.")
        rtn_list = []
        for obj in points:
            rtn_list.append(self.distanceFrom(obj))
        return points[rtn_list.index(min(rtn_list))]

    def clone(self):
        return PointND(*self.t[0:len(self.t)])

    def __add__(self, other):
        newArgs = []
        if type(other) is float:
           newList = [i+other for i in self.t]
           return PointND(*newList[0:len(newList)])
        if type(other) is PointND:
            for i,j in zip(self.t, other.t):
                newArgs.append(i+j)
            return PointND(*newArgs[0:len(newArgs)])
        else:
            raise ValueError("Input is neither a float nor a PointND!")

    def __sub__(self, other):
        newArgs = []
        if type(other) is float:
           newList = [i-other for i in self.t]
           return PointND(*newList[0:len(newList)])
        elif type(other) is PointND:
            for i,j in zip(self.t, other.t):
                newArgs.append(i-j)
            return PointND(*newArgs[0:len(newArgs)])
        else:
            raise ValueError("Input is neither a float nor a PointND!")

    def __mul__(self, other):
        newList = [i*other for i in self.t]
        return PointND(*newList[0:len(newList)])

    def __truediv__(self, other):
        newList = [i/other for i in self.t]
        return PointND(*newList[0:len(newList)])

    def __neg__(self):
        newList = [-i for i in self.t]
        return PointND(*newList[0:len(newList)])

    def __getitem__(self, item):
        newList = [i for i in self.t]
        return newList[item]

    def __eq__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        selfList = [i for i in self.t]
        otherList = [i for i in other.t]
        if (selfList == otherList):
            return True
        else:
            return False

    def __ne__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        if (self == other):
            return False
        else:
            return True

    def __gt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        newList = [0.0 for x in range(0, self.n)]
        origin = PointND(*newList[0:self.n])
        distanceSelfOrigin = self.distanceFrom(origin)
        distanceOtherOrigin = other.distanceFrom(origin)
        if distanceSelfOrigin > distanceOtherOrigin:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        newList = [0.0 for x in range(0, self.n)]
        origin = PointND(*newList[0:self.n])
        distanceSelfOrigin = self.distanceFrom(origin)
        distanceOtherOrigin = other.distanceFrom(origin)
        if distanceSelfOrigin >= distanceOtherOrigin:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        newList = [0.0 for x in range(0, self.n)]
        origin = PointND(*newList[0:self.n])
        distanceSelfOrigin = self.distanceFrom(origin)
        distanceOtherOrigin = other.distanceFrom(origin)
        if distanceSelfOrigin < distanceOtherOrigin:
            return True
        else:
            return False

    def __le__(self, other):
        if self.n != other.n:
            raise ValueError("Cannot compare points with different cardinalities.")
        newList = [0.0 for x in range(0, self.n)]
        origin = PointND(*newList[0:self.n])
        distanceSelfOrigin = self.distanceFrom(origin)
        distanceOtherOrigin = other.distanceFrom(origin)
        if distanceSelfOrigin <= distanceOtherOrigin:
            return True
        else:
            return False

class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        PointND.__init__(self, x, y, z)

class PointGroup:

    def __init__(self, **kwargs):
        self._pointMap = dict()
        self.n = int
        if (len(kwargs) is 0):
            self._pointMap = {}
            self.n = 0
        elif "pointList" in kwargs:
            if (len(kwargs["pointList"]) is 0):
                raise ValueError("'pointList' input parameter cannot be empty.")

            for pointND in kwargs["pointList"]:
                self._pointMap[pointND.__hash__()] = pointND

            #Set the group's cardinality to the first point's cardinality
            self.n = self._pointMap[list(self._pointMap)[0]].n

            for hashVal in self._pointMap:
                if self._pointMap[hashVal].n != self.n:
                    raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(self._pointMap[hashVal], self.n))

        else:
            raise KeyError("'pointList' input parameter not found.")
    def addPoint(self, point):
        if point.n != self.n:
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))
        self._pointMap[point.__hash__()] = point

    def count(self):
        return len(self._pointMap)

    def computeBoundingHyperCube(self):
        maxList = []
        minList = []
        cardiList = [[] for i in range(0,self.n)]
        for point in self._pointMap:
             for index in range(0,self.n):
                cardiList[index].append(self._pointMap[point].t[index])
        for element in cardiList:
            maxList.append(max(element))
            minList.append(min(element))
        return((PointND(*minList[0:len(minList)]),PointND(*maxList[0:len(maxList)])))

    def computeNearestNeighbors(self, otherPointGroup):
        listOfTuples = []
        for thisPoint,otherPoint in zip(self._pointMap.values(),otherPointGroup._pointMap.values()):
            thesePoints = [point for point in self._pointMap.values()]
            otherPoints = [point for point in otherPointGroup._pointMap.values()]
        for point in thesePoints:
             listOfTuples.append((point.t, point.nearestPoint(otherPoints).t))
        listOfTuples.sort()
        return(listOfTuples)

    def __iter__(self):
         return iter(self._pointMap.values())

    def __add__(self, other):
        if (self.n != other.n):
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(other, self.n))
        self.addPoint(other)
        return self

    def __sub__(self, other):
        if (other.__hash__() in self._pointMap):
            del self._pointMap[other.__hash__()]
        return self

    def __contains__(self, point):
        if (point.__hash__() in self._pointMap):
            return True
        return False


if __name__ == "__main__":
    origin = PointND(0.0, 0.0, 0.0)
    point1 = PointND(5.3, 4.5, 3.2)
    point2 = PointND(1.1, 2.2, 3.3)
    point3 = PointND(1.0, 1.0, 1.0)
    point4 = PointND(2.0, 1.0, 1.0)
    point5 = PointND(1.2, 2.0, 3.2)
    point6 = PointND(6.1, 2.2, 3.3)
    point7 = PointND(4.0, 8.0, 8.0)
    point8 = PointND(5.8, 1.0, 1.0)
    pointKillMe = PointND(2.2, 5.1, 8.5)
    breakMe = PointND(1.0, 2.0, 3.0, 4.0)
    pointList2 = [point1, point2, point3, point4]
    pointList3 = [point1, point2, point3, point4, breakMe]
    nearestPt = origin.nearestPoint(pointList2)
    testPt = PointND(1.0, 2.0, 3.0)

    joke = point2.nearestPoint(pointList2)
    point5 = testPt.clone()
    pointAdd = point1+5.2
    pointSub = point1-origin
    pointMul = point4*3.2
    pointDiv = point4/0.6
    print(pointDiv.__str__())
    pointNeg = -point1
    itemOne = point3[0]
    my3D = Point3D(1.1, 2.2, 3.3)
    newGroup = PointGroup(pointList = pointList2)
    otherGroup = PointGroup(pointList = [point5, point6, point7, point8])
    otherGroup+testPt
    otherGroup+pointMul
    print(otherGroup._pointMap)
    otherGroup-pointAdd
    otherGroup-pointMul
    print(otherGroup._pointMap)
    print(point1 in otherGroup)
    pointTuple = newGroup.computeBoundingHyperCube()
    newGroup.computeNearestNeighbors(otherGroup)
   # for i in otherGroup._pointMap.values():
       # print(i.t)

    #print(pointAdd.t)
    #print(pointSub.t)
    #print(pointMul.t)
    #print(pointDiv.t)
    #print(pointNeg.t)
    #print(itemOne)
    #print(point4 == point1)
    #print(point4 != point5)
    #print(point1 > point2)
    #print(point4 >= point3)
    #print(point4 < point1)
    #print(point1 <= point4)
    #print(point5.t)
    #point1.__str__()
    #print(point1.distanceFrom(y))