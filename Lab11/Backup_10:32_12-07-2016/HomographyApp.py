import sys
import re
from PySide.QtCore import *
from PySide.QtGui import *
from HomographyGUI import *
from Homography import *

class Consumer(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        #ATTRIBUTES#

        #Make sure that QEdit boxes are read only!
        self.pointBox1.setReadOnly(True)
        self.pointBox2.setReadOnly(True)
        self.pointBox3.setReadOnly(True)
        self.pointBox3.setReadOnly(True)

        #INITIALIZATIONS#
        self.PointBox = None
        self.TargetView.mousePressEvent = self.getPoints
        self.toggleAll(False)
        self.SourceLoad.clicked.connect(self.loadSourceData)
        self.TargetLoad.clicked.connect(self.loadTargetData)
        self.PointButton.clicked.connect(self.checkPoints)
        self.TransformButton.clicked.connect(self.doTransform)
        self.ResetButton.clicked.connect(self.resetAll)
        self.SaveButton.clicked.connect(self.saveImage)
        self.state = "Idle"

        #Disable everything except the topmost load buttons
    def resetAll(self):
        if self.state == "Transformed":
            self.toggleAll(True)
            self.loadTargetImgFromFile(self.tgtPath)
           # self.pointBox1.setText("")
         #   self.pointBox2.setText("")
          #  self.pointBox3.setText("")
         #   self.pointBox4.setText("")

    def getPoints(self, QMouseEvent):
        super(Consumer, self).mousePressEvent(QMouseEvent)
        if self.PointButton.isChecked():
           x = self.TargetView.mapToScene(QMouseEvent.pos()).x()
           y = self.TargetView.mapToScene(QMouseEvent.pos()).y()
           if (x < self.tgtimg.width() and x > 0) and (y > 0 and y < self.tgtimg.height()):
              if self.PointBox == 1:
                   self.PointBox += 1
                   self.pointBox1.setText("{:.1f}, {:.1f}".format(x,y))
              elif self.PointBox == 2:
                   self.PointBox += 1
                   self.pointBox2.setText("{:.1f}, {:.1f}".format(x,y))
              elif self.PointBox == 3:
                   self.PointBox += 1
                   self.pointBox3.setText("{:.1f}, {:.1f}".format(x,y))
              elif self.PointBox == 4:
                   self.PointBox += 1
                   self.pointBox4.setText("{:.1f}, {:.1f}".format(x,y))

    def saveImage(self):
        filePath, _ = QFileDialog.getSaveFileName(self, caption='Save PNG file ...', filter="PNG files (*.png)")
        filePath += ".png"
        if not filePath:
            return
        self.tgtimg.save(filePath, "PNG")

    def doTransform(self):
        sourceImg = np.asarray(self.SourceArray, dtype=np.float64)
        if len(sourceImg.shape) == 3:
            trans = ColorTransformation(sourceImg)
        else:
            trans = Transformation(sourceImg)
        effect = None
        if self.EffectList.currentText() == "Rotate 90°":
            effect = Effect.rotate90
        if self.EffectList.currentText() == "Rotate 180°":
            effect = Effect.rotate180
        if self.EffectList.currentText() == "Rotate 270°":
            effect = Effect.rotate270
        if self.EffectList.currentText() == "Flip Vertically":
            effect = Effect.flipVertically
        if self.EffectList.currentText() == "Flip Horizontally":
            effect = Effect.flipHorizontally
        if self.EffectList.currentText() == "Transpose":
            effect = Effect.transpose

        x1,y1 = re.findall(r"\d+\.\d", self.pointBox1.text())
        x2,y2 = re.findall(r"\d+\.\d", self.pointBox2.text())
        x3,y3 = re.findall(r"\d+\.\d", self.pointBox3.text())
        x4,y4 = re.findall(r"\d+\.\d", self.pointBox4.text())
        targetPoints = np.array([[float(x1), float(y1)], [float(x2), float(y2)], [float(x3), float(y3)], [float(x4), float(y4)]], np.float64)
        trans.setupTransformation(targetPoints, effect)
        output = trans.transformImageOnto(self.targetArray)
        outImage = Image.fromarray(output)
        imsave("guiTest.png", outImage)
        self.state = "Transformed"
        self.loadTargetImgFromFile("guiTest.png")
        self.SourceLoad.setEnabled(True)
        self.TargetLoad.setEnabled(True)
        self.PointButton.setDisabled(True)
        self.pointBox1.setDisabled(True)
        self.pointBox2.setDisabled(True)
        self.pointBox3.setDisabled(True)
        self.pointBox4.setDisabled(True)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace and self.PointButton.isChecked() and self.PointBox > 1:
            if self.PointBox == 2:
                self.PointBox -= 1
                self.pointBox1.setText("")
            elif self.PointBox == 3:
                self.PointBox -= 1
                self.pointBox2.setText("")
            elif self.PointBox == 4:
                self.PointBox -= 1
                self.pointBox3.setText("")
            else:
                self.PointBox -= 1
                self.pointBox4.setText("")
    def checkPoints(self):
        if self.PointButton.isChecked():
            self.state = "Point"
            self.SourceLoad.setDisabled(True)
            self.TargetLoad.setDisabled(True)
            self.EffectList.setDisabled(True)
            self.effectLabel.setDisabled(True)
            self.TransformButton.setDisabled(True)
            self.ResetButton.setDisabled(True)
            self.SaveButton.setDisabled(True)
            self.PointBox = 1
            self.pointBox1.setText("")
            self.pointBox2.setText("")
            self.pointBox3.setText("")
            self.pointBox4.setText("")
        else:
            if self.PointBox != 5:
                self.pointBox1.setText("")
                self.pointBox2.setText("")
                self.pointBox3.setText("")
                self.pointBox4.setText("")
                self.SourceLoad.setEnabled(True)
                self.TargetLoad.setEnabled(True)
                self.PointBox = None
                self.state = "Loaded"
            else:
                self.toggleAll(True)
                self.state = "Ready"
                self.SourceLoad.setEnabled(True)
                self.TargetLoad.setEnabled(True)

    def toggleAll(self, state):
        self.pointBox1.setEnabled(state)
        self.pointBox2.setEnabled(state)
        self.pointBox3.setEnabled(state)
        self.pointBox4.setEnabled(state)
        self.PointButton.setEnabled(state)
        self.TransformButton.setEnabled(state)
        self.ResetButton.setEnabled(state)
        self.SaveButton.setEnabled(state)
        self.EffectList.setEnabled(state)
        self.effectLabel.setEnabled(state)
        self.SourceView.setEnabled(state)
        self.TargetView.setEnabled(state)

    def loadSourceData(self):
        if self.state != "Ready":
            self.state = "Loaded"
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open PNG file', filer = "PNG files (*.png)")
        if not filePath:
            return
        self.srcPath = filePath
        self.loadSourceImgFromFile(filePath)

    def loadTargetData(self):
        self.state = "Loaded"
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open PNG file', filer = "PNG files (*.png)")
        if not filePath:
            return
        self.tgtPath = filePath
        self.loadTargetImgFromFile(filePath)

    def loadSourceImgFromFile(self, filePath):
        self.SourceArray = imread(filePath)
        self.srcimg = QImage(filePath)
        pixMap = QPixmap.fromImage(self.srcimg)
        self.sourcePix = pixMap
        scn = QGraphicsScene()
        scn.addPixmap(pixMap)
        self.SourceView.setScene(scn)
        self.SourceView.fitInView(scn.sceneRect(), Qt.KeepAspectRatio)
        self.checkIfBothLoaded()

    def loadTargetImgFromFile(self, filePath):
        self.tgtimg = QImage(filePath)
        self.targetArray = imread(filePath)
        pixMap = QPixmap.fromImage(self.tgtimg)
        scn = QGraphicsScene()
        scn.addPixmap(pixMap)
        self.TargetView.setScene(scn)
        self.TargetView.fitInView(scn.sceneRect(), Qt.KeepAspectRatio)
        self.checkIfBothLoaded()

    def resetTarget(self):
        self.tgtimg = QImage(self.tgtPath)
        self.targetArray = imread(self.tgtPath)
        pixMap = QPixmap.fromImage(self.tgtimg)
        scn = QGraphicsScene()
        scn.addPixmap(pixMap)
        self.TargetView.setScene(scn)
        self.TargetView.fitInView(scn.sceneRect(), Qt.KeepAspectRatio)

    def checkIfBothLoaded(self):
        if len(self.SourceView.items()) is not 0 and len(self.TargetView.items()) is not 0:
            self.setLoadedState()

    def setLoadedState(self):
        self.pointBox1.setEnabled(True)
        self.pointBox2.setEnabled(True)
        self.pointBox3.setEnabled(True)
        self.pointBox4.setEnabled(True)
        self.PointButton.setEnabled(True)
        self.PointButton.setCheckable(True)
        self.TargetView.setEnabled(True)
        self.SourceView.setEnabled(True)
        self.ResetButton.setDisabled(True)
        self.SaveButton.setDisabled(True)
        self.TransformButton.setDisabled(True)
        self.EffectList.setDisabled(True)

        if (self.state == "Transformed"):
            self.ResetButton.setEnabled(True)
            self.SaveButton.setEnabled(True)
            self.TransformButton.setEnabled(True)
            self.EffectList.setEnabled(True)

        if (self.state == "Loaded"):
            self.resetTarget()
            self.ResetButton.setDisabled(True)
            self.SaveButton.setDisabled(True)
            self.TransformButton.setDisabled(True)
            self.EffectList.setDisabled(True)
            self.PointBox = 1
            self.pointBox1.setText("")
            self.pointBox2.setText("")
            self.pointBox3.setText("")
            self.pointBox4.setText("")
if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()
    currentForm.show()
    currentApp.exec_()