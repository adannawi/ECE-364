from enum import Enum
import numpy as np
from scipy.misc import *
from scipy.interpolate import *
from scipy import *
from PIL import Image
class Effect(Enum):
    rotate90 = 1
    rotate180 = 2
    rotate270 = 3
    flipHorizontally = 4
    flipVertically = 5
    transpose = 6

class Homography:
    def __init__(self, **kwargs):

        if "homographyMatrix" in kwargs and kwargs["homographyMatrix"] is not None:
            if type(kwargs["homographyMatrix"][0][0]) is not np.float64:
                raise ValueError("Input matrix is not of type 'np.float64'!")
            if len(kwargs["homographyMatrix"]) is not len(kwargs["homographyMatrix"][0]):
                raise ValueError("Input matrix dimensions do not match!")
            self.forwardMatrix = kwargs["homographyMatrix"]
            self.inverseMatrix = np.linalg.inv(self.forwardMatrix)

        if "sourcePoints" in kwargs and "targetPoints" in kwargs:
            if type(kwargs["sourcePoints"][0][0]) is not np.float64:
                raise ValueError("sourcePoints matrix is not of type 'np.float64'!")
            if type(kwargs["targetPoints"][0][0]) is not np.float64:
                raise ValueError("targetPoints matrix is not of type 'np.float64'!")
            if len(kwargs["sourcePoints"]) is not 4 or len(kwargs["sourcePoints"][0]) is not 2:
                raise ValueError("sourcePoints is not a 4x2 matrix!")
            if len(kwargs["targetPoints"]) is not 4 or len(kwargs["targetPoints"][0]) is not 2:
                raise ValueError("targetPoints is not a 4x2 matrix!")
            if "effect" in kwargs and kwargs["effect"] is not None:
                if not isinstance(kwargs["effect"], Enum):
                    raise TypeError("Given effect is not an instance of Effect enum!")
                self.computeHomography(kwargs["sourcePoints"],kwargs["targetPoints"],kwargs["effect"])
            self.computeHomography(kwargs["sourcePoints"],kwargs["targetPoints"])

        if ("sourcePoints" not in kwargs or "targetPoints" not in kwargs) and "homographyMatrix" not in kwargs:
            raise ValueError("Missing or invalid parameters")

    def computeHomography(self, sourcePoints, targetPoints, effect=None):

        tempPt1 = sourcePoints[0].copy()
        tempPt2 = sourcePoints[1].copy()
        tempPt3 = sourcePoints[2].copy()
        tempPt4 = sourcePoints[3].copy()

        if effect == Effect.rotate90:
            sourcePoints[0] = tempPt3
            sourcePoints[1] = tempPt1
            sourcePoints[2] = tempPt4
            sourcePoints[3] = tempPt2

        if effect == Effect.rotate180:
            sourcePoints[0] = tempPt4
            sourcePoints[1] = tempPt3
            sourcePoints[2] = tempPt2
            sourcePoints[3] = tempPt1

        if effect == Effect.rotate270:
            sourcePoints[0] = tempPt2
            sourcePoints[1] = tempPt4
            sourcePoints[2] = tempPt1
            sourcePoints[3] = tempPt3

        if effect == Effect.flipVertically:
            sourcePoints[0] = tempPt2
            sourcePoints[1] = tempPt1
            sourcePoints[2] = tempPt4
            sourcePoints[3] = tempPt3

        if effect == Effect.flipHorizontally:
            sourcePoints[0] = tempPt3
            sourcePoints[1] = tempPt4
            sourcePoints[2] = tempPt1
            sourcePoints[3] = tempPt2

        if effect == Effect.transpose:
            sourcePoints[0] = tempPt1
            sourcePoints[1] = tempPt3
            sourcePoints[2] = tempPt2
            sourcePoints[3] = tempPt4

        A1 = np.array([[sourcePoints[0][0], sourcePoints[0][1], 1, 0, 0, 0, (-(targetPoints[0][0]*sourcePoints[0][0])),
                        (-(targetPoints[0][0]*sourcePoints[0][1]))],[0, 0, 0, sourcePoints[0][0], sourcePoints[0][1], 1,
                                                                     (-(targetPoints[0][1]*sourcePoints[0][0])), (-(targetPoints[0][1]*sourcePoints[0][1]))]], dtype=np.float64)
        b1 = np.array([[targetPoints[0][0]],[targetPoints[0][1]]], dtype=np.float64)

        A2 = np.array([[sourcePoints[1][0], sourcePoints[1][1], 1, 0, 0, 0, (-(targetPoints[1][0]*sourcePoints[1][0])),
                        (-(targetPoints[1][0]*sourcePoints[1][1]))],[0, 0, 0, sourcePoints[1][0], sourcePoints[1][1], 1,
                                                                     (-(targetPoints[1][1]*sourcePoints[1][0])), (-(targetPoints[1][1]*sourcePoints[1][1]))]], dtype=np.float64)
        b2 = np.array([[targetPoints[1][0]],[targetPoints[1][1]]], dtype=np.float64)

        A3 = np.array([[sourcePoints[2][0], sourcePoints[2][1], 1, 0, 0, 0, (-(targetPoints[2][0]*sourcePoints[2][0])),
                        (-(targetPoints[2][0]*sourcePoints[2][1]))],[0, 0, 0, sourcePoints[2][0], sourcePoints[2][1], 1,
                                                                     (-(targetPoints[2][1]*sourcePoints[2][0])), (-(targetPoints[2][1]*sourcePoints[2][1]))]], dtype=np.float64)
        b3 = np.array([[targetPoints[2][0]],[targetPoints[2][1]]], dtype=np.float64)

        A4 = np.array([[sourcePoints[3][0], sourcePoints[3][1], 1, 0, 0, 0, (-(targetPoints[3][0]*sourcePoints[3][0])),
                        (-(targetPoints[3][0]*sourcePoints[3][1]))],[0, 0, 0, sourcePoints[3][0], sourcePoints[3][1], 1,
                                                                     (-(targetPoints[3][1]*sourcePoints[3][0])), (-(targetPoints[3][1]*sourcePoints[3][1]))]], dtype=np.float64)
        b4 = np.array([[targetPoints[3][0]],[targetPoints[3][1]]], dtype=np.float64)

        A = np.vstack((A1, A2, A3, A4))
        b = np.vstack((b1, b2, b3, b4))
        h = np.linalg.solve(A,b)
        hNew = np.array([[h[0][0],h[1][0],h[2][0]],[h[3][0],h[4][0],h[5][0]],[h[6][0],h[7][0],1]])
        hInv = np.linalg.inv(hNew)

        self.forwardMatrix = hNew
        self.inverseMatrix = hInv

class Transformation:
    def __init__(self, sourceImage, homography=None):
        if type(sourceImage) is not np.ndarray:
            raise TypeError("Image is not of type 'ndarray'!")
        if homography is not None and not isinstance(homography, Homography):
            raise TypeError("Given homography is not of type Homography!")
        self.sourceImage = sourceImage
        self.lengthX = len(sourceImage[0])
        self.lengthY = len(sourceImage)
        self.homography = homography

    def setupTransformation(self, targetPoints, effect=None):

        if self.homography is None:
            sourcePts = np.array([[0, 0], [len(self.sourceImage[0])-1, 0], [0, len(self.sourceImage)-1], [len(self.sourceImage[0])-1, len(self.sourceImage)-1]], dtype=np.float64)
            impromptuHomography = Homography(sourcePoints=sourcePts, targetPoints=targetPoints, effect=effect)
            self.homography = impromptuHomography

        self.targetPoints = targetPoints
        self.minX = targetPoints[0][0]
        self.maxX = targetPoints[0][0]
        self.minY = targetPoints[0][1]
        self.maxY = targetPoints[0][1]

        for points in targetPoints:
            x = points[0]
            y = points[1]

            if self.minX >= x:
                self.minX = x
            if self.maxX <= x:
                self.maxX = x
            if self.minY >= y:
                self.minY = y
            if self.maxY <= y:
                self.maxY = y

        self.xArr = np.arange(self.lengthX)
        self.yArr = np.arange(self.lengthY)

    def transformImageOnto(self, containerImage):
        if type(containerImage) is not np.ndarray:
            raise TypeError("Image is not of type 'ndarray'!")
        spl = RectBivariateSpline(self.yArr, self.xArr, self.sourceImage, kx=1, ky=1)
        for x in arange(self.minX, self.maxX+1):
            for y in arange(self.minY, self.maxY+1):
                newXY = np.dot(self.homography.inverseMatrix, np.array([[x],[y],[1]], dtype=np.float64))
                newXY = np.round(newXY/newXY[2], 3)
                if newXY[0] <= self.lengthX-1 and newXY[0] >= 0 and newXY[1] <= self.lengthY-1 and newXY[1] >= 0:
                    oldXY = spl(newXY[1], newXY[0])
                    containerImage[y][x] = np.uint8(np.round(oldXY))
        return containerImage



        #imsave("test3.png", containerImage)

class ColorTransformation(Transformation):
    def __init__(self, sourceImage, homography=None):
        Transformation.__init__(self, sourceImage, homography)
        if type(self.sourceImage[0][0]) is not np.uint8:
            if len(self.sourceImage[0][0]) <= 1:
                raise ValueError("Image is not color")
        else:
            raise ValueError("Image is not color")

    def transformImageOnto(self, containerImage):
        if type(containerImage) is not np.ndarray:
            raise TypeError("Image is not of type 'ndarray'!")

        splR = RectBivariateSpline(self.yArr, self.xArr, self.sourceImage[:,:,0], kx=1, ky=1)
        splG = RectBivariateSpline(self.yArr, self.xArr, self.sourceImage[:,:,1], kx=1, ky=1)
        splB = RectBivariateSpline(self.yArr, self.xArr, self.sourceImage[:,:,2], kx=1, ky=1)

        for x in arange(self.minX, self.maxX+1):
            for y in arange(self.minY, self.maxY+1):
                newXY = np.dot(self.homography.inverseMatrix, np.array([[x],[y],[1]], dtype=np.float64))
                newXY = np.round(newXY/newXY[2], 3)
                if newXY[0] <= self.lengthX-1 and newXY[0] >= 0 and newXY[1] <= self.lengthY-1 and newXY[1] >= 0:

                    oldXYR = splR(newXY[1], newXY[0])
                    oldXYG = splG(newXY[1], newXY[0])
                    oldXYB = splB(newXY[1], newXY[0])

                    containerImage[y,x,0] = np.uint8(np.round(oldXYR))
                    containerImage[y,x,1] = np.uint8(np.round(oldXYG))
                    containerImage[y,x,2] = np.uint8(np.round(oldXYB))

        return containerImage

class AdvancedTransformation:
    def __init__(self, sourceImage, v, h1, h2):
        if type(sourceImage) is not np.ndarray:
            raise TypeError("Image is not of type 'ndarray'!")

        if type(sourceImage[0][0]) is not np.uint8:
            if len(sourceImage[0][0]) <= 1:
                raise ValueError("Image is not color")
        else:
            raise ValueError("Image is not color")

        if ((len(sourceImage[0]))% 2) is not 0:
            raise ValueError("x dimension of image is not even!")

        self.sourceImage = sourceImage
        self.v = v
        self.h1 = h1
        self.h2 = h2

    def applyEffectV(self):
        firstHalf,secondHalf = np.split(self.sourceImage, 2, 1)
        h1 = self.h1
        h2 = self.h2
        v = self.v
        firstLeftTargets = np.array([[0, 0], [len(firstHalf[0])-1-h2, v], [h1, len(firstHalf)-1], [len(firstHalf[0])-1, len(firstHalf)+v-1]], dtype=np.float64)
        firstLeftSources = np.array([[0, 0], [len(firstHalf[0])-1, 0], [0, len(firstHalf)-1], [len(firstHalf[0])-1, len(firstHalf)-1]], dtype=np.float64)
        leftHomo = Homography(sourcePoints=firstLeftSources, targetPoints=firstLeftTargets)
        colorTrans = ColorTransformation(firstHalf, leftHomo)
        colorTrans.setupTransformation(firstLeftTargets)

        target_firstHalfR = np.ones((len(firstHalf)+v,len(firstHalf[0])))
        target_firstHalfG = np.ones((len(firstHalf)+v,len(firstHalf[0])))
        target_firstHalfB = np.ones((len(firstHalf)+v,len(firstHalf[0])))
        target_firstHalf = np.dstack((target_firstHalfR, target_firstHalfG, target_firstHalfB))
        target_firstHalf[target_firstHalf < 255] = 255

        secondRightTargets = np.array([[h2, v], [len(secondHalf[0])-1, 0], [0, len(secondHalf)+v-1], [len(secondHalf[0])-1-h1, len(secondHalf)-1]], dtype=np.float64)
        secondRightSources = np.array([[0, 0], [len(secondHalf[0])-1, 0], [0, len(secondHalf)-1], [len(secondHalf[0])-1, len(secondHalf)-1]], dtype=np.float64)
        rightHomo = Homography(sourcePoints=secondRightSources, targetPoints=secondRightTargets)
        colorTrans2 = ColorTransformation(secondHalf, rightHomo)
        colorTrans2.setupTransformation(secondRightTargets)

        target_secondHalfR = np.ones((len(secondHalf)+v,len(secondHalf[0])))
        target_secondHalfG = np.ones((len(secondHalf)+v,len(secondHalf[0])))
        target_secondHalfB = np.ones((len(secondHalf)+v,len(secondHalf[0])))
        target_secondHalf = np.dstack((target_secondHalfR, target_secondHalfG, target_secondHalfB))
        target_secondHalf[target_secondHalf < 255] = 255

        resultImageLeft = colorTrans.transformImageOnto(target_firstHalf)
        resultImageRight = colorTrans2.transformImageOnto(target_secondHalf)

        resultImage = np.hstack((resultImageLeft, resultImageRight))
        return resultImage

    def applyEffectA(self):
        firstHalf, secondHalf = np.split(self.sourceImage, 2, 1)
        h1 = self.h1
        h2 = self.h2
        v = self.v
        firstLeftTargets = np.array([[h1, v], [len(firstHalf[0])-1, 0], [0, len(firstHalf)-1+v], [len(firstHalf[0])-1-h2, len(firstHalf)-1]], dtype=np.float64)
        firstLeftSources = np.array([[0, 0], [len(firstHalf[0])-1, 0], [0, len(firstHalf)-1], [len(firstHalf[0])-1, len(firstHalf)-1]], dtype=np.float64)
        leftHomo = Homography(sourcePoints=firstLeftSources, targetPoints=firstLeftTargets)
        colorTrans = ColorTransformation(firstHalf, leftHomo)
        colorTrans.setupTransformation(firstLeftTargets)
        target_firstHalfR = np.ones((len(firstHalf)+v,len(firstHalf[0])))
        target_firstHalfG = np.ones((len(firstHalf)+v,len(firstHalf[0])))
        target_firstHalfB = np.ones((len(firstHalf)+v,len(firstHalf[0])))
        target_firstHalf = np.dstack((target_firstHalfR, target_firstHalfG, target_firstHalfB))
        target_firstHalf[target_firstHalf < 255] = 255

        secondRightTargets = np.array([[0, 0], [len(secondHalf[0])-1-h1, v], [h2, len(secondHalf)-1], [len(secondHalf[0])-1, len(secondHalf)-1+v]], dtype=np.float64)
        secondRightSources = np.array([[0, 0], [len(secondHalf[0])-1, 0], [0, len(secondHalf)-1], [len(secondHalf[0])-1, len(secondHalf)-1]], dtype=np.float64)
        rightHomo = Homography(sourcePoints=secondRightSources, targetPoints=secondRightTargets)
        colorTrans2 = ColorTransformation(secondHalf, rightHomo)
        colorTrans2.setupTransformation(secondRightTargets)

        target_secondHalfR = np.ones((len(secondHalf)+v,len(secondHalf[0])))
        target_secondHalfG = np.ones((len(secondHalf)+v,len(secondHalf[0])))
        target_secondHalfB = np.ones((len(secondHalf)+v,len(secondHalf[0])))
        target_secondHalf = np.dstack((target_secondHalfR, target_secondHalfG, target_secondHalfB))
        target_secondHalf[target_secondHalf < 255] = 255

        resultImageLeft = colorTrans.transformImageOnto(target_firstHalf)
        resultImageRight = colorTrans2.transformImageOnto(target_secondHalf)

        resultImage = np.hstack((resultImageLeft, resultImageRight))
        return resultImage

if __name__ == "__main__":
  #  a = np.float64(2.4)
  #  targetPoints = np.array([[600, 50], [1550, 500], [50, 400], [800, 1150.0]])
   # srcMtrx = np.array([[1.23, 2.34], [1.1, 3.3], [4.21, 4.32], [1.4, 7.6]], dtype=np.float64)
   # tgtMtrx = np.array([[1.53, 2.34], [1.9, 3.3], [2.5, 4.32], [9.9, 7.6]], dtype=np.float64)
   # homoMtrx = np.array([[-1.73, -1.19e-02, 2.34], [-3.01, 1.87, 3.93], [-7.1, -3.04, 1]], dtype=np.float64)
    sourceImg = imread("TestImages/knight.png")
    colorImg = imread("TestImages/Ring.png")
    targetImg = imread("TestImages/White.png")
    actualImg = imread("test3.png")
    expectedImg = imread("TestImages/Target_knight_transpose.png")
   # diff = np.absolute(expectedImg, actualImg)
   # bool_diff = np.logical_and(diff, np.ones(expectedImg.shape, dtype=np.uint8))
    #diffImg = 255 * bool_diff
    #imsave('test_diff.png', diffImg)
    #newEffect = Effect.transpose
    #newHomo = Homography(homographyMatrix=homoMtrx)
    #newTransformation = Transformation(sourceImg)
    #newTransformation.setupTransformation(targetPoints, newEffect)
    #colorTrans = ColorTransformation(colorImg)
    #colorTrans.setupTransformation(targetPoints)
    #targetClr = colorTrans.transformImageOnto(targetImg)
    #imsave("testColor.png", targetClr)
    #newAdv = AdvancedTransformation(colorImg, 100, 0, 0)
    #myV = newAdv.applyEffectA()
    #imsave("resultRing.png", myV)
    #actualValue = myV
    #expectedValue = imread("TestImages/Ring_EffectV_100_000_000.png")
   # diff = np.absolute(expectedValue, actualValue)
   # bool_diff = np.logical_and(diff, np.ones(expectedValue.shape, dtype=np.uint8))
   # diffImg = 255 * bool_diff
    #imsave('test_diff.png', diffImg)
       # dotMatrixX = arange(self.minX, self.maxX+1)
      #  dotMatrixY = arange(self.minY, self.maxY+1)
      #  dotMatrix = np.array([dotMatrixX, dotMatrixY, [1]], dtype=np.float64)
    testArrX = arange(0,20)
    testArrY = arange(20,40)
    testArr = np.vstack((testArrX, testArrY))
    print(testArr)

