from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *
import re

class Calculator(QMainWindow, Ui_Calculator):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setupUi(self)
        self.currentValue = ""
        self.value1 = 0
        self.value2 = 0
        self.isPending = False
        self.operation = ""
        self.decimalDigits = self.cboDecimal.currentText()
        self.thousandSeparator = True
        self.buttons = [self.btn0, self.btn1, self.btn2, self.btn3, self.btn4,
        self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        for button in self.buttons:
            button.clicked.connect(self.readInput)
        self.btnDot.clicked.connect(self.addDecimal)
        self.btnPlus.clicked.connect(self.onAdd)
        self.btnEqual.clicked.connect(self.onEqual)
        self.btnMinus.clicked.connect(self.onSubtract)
        self.btnClear.clicked.connect(self.clearAll)
        self.chkSeparator.stateChanged.connect(self.setSeparator)
        self.cboDecimal.activated.connect(self.updateDecimal)
        self.btnMultiply.clicked.connect(self.onMultiply)
        self.btnDivide.clicked.connect(self.onDivide)

    def addDecimal(self):
        self.currentValue = str(self.currentValue)+"."

    def updateDecimal(self):
        self.decimalDigits = self.cboDecimal.currentText()
        self.txtDisplay.setText("{:.{dcml}f}".format(float(self.currentValue), dcml = self.decimalDigits))
        print("Current decimalDigits = ", self.decimalDigits)

    def setSeparator(self):
        if self.chkSeparator.isChecked():
            self.thousandSeparator = True
        else:
            self.thousandSeparator = False

    def clearAll(self):
        self.currentValue = ""
        self.value1 = 0
        self.value2 = 0
        self.operation = ""
        self.isPending = False
        self.txtDisplay.setText("0.")

    def readInput(self):
        if len(str(self.currentValue)) < 12:
            self.currentValue = str(self.currentValue)+self.sender().text()
        self.txtDisplay.setText(str(self.currentValue))


    def calculate(self):
        if self.isPending:
            self.value2 = self.currentValue

            if self.operation == "add":
                result = float(self.value1)+float(self.value2)
                self.isPending = False
                self.operation = ""
                self.currentValue = result
                self.txtDisplay.setText("{:.{dcml}f}".format(float(self.currentValue), dcml = self.decimalDigits))

            if self.operation == "subtract":
                result = float(self.value1)-float(self.value2)
                self.isPending = False
                self.operation = ""
                self.currentValue = result
                self.txtDisplay.setText("{:.{dcml}f}".format(float(self.currentValue), dcml = self.decimalDigits))

            if self.operation == "multiply":
                result = float(self.value1)*float(self.value2)
                self.isPending = False
                self.operation = ""
                self.currentValue = result
                self.txtDisplay.setText("{:.{dcml}f}".format(float(self.currentValue), dcml = self.decimalDigits))

            if self.operation == "divide":
                try:
                    result = float(self.value1)/float(self.value2)
                    self.currentValue = result
                    self.txtDisplay.setText("{:.{dcml}f}".format(float(self.currentValue), dcml = self.decimalDigits))
                except:
                    self.isPending = False
                    self.operation = ""
                    print("Easy there, Satan! You can't divide by 0!")
        if self.thousandSeparator:
            splitNumber = self.txtDisplay.text().split(".")
            if len(splitNumber[0]) > 3:
                self.txtDisplay.setText("{:,}.{}".format(int(splitNumber[0]), splitNumber[1]))



    def onAdd(self):
        if self.isPending:
            self.calculate()
        self.isPending = True
        self.operation = "add"
        self.value1 = self.currentValue
        self.txtDisplay.clear()
        self.currentValue = ""

    def onEqual(self):
        if self.isPending:
            self.calculate()

    def onSubtract(self):
        if self.isPending:
            self.calculate()
        self.isPending = True
        self.operation = "subtract"
        self.value1 = self.currentValue
        self.txtDisplay.clear()
        self.currentValue = ""

    def onMultiply(self):
        if self.isPending:
            self.calculate()
        self.isPending = True
        self.operation = "multiply"
        self.value1 = self.currentValue
        self.txtDisplay.clear()
        self.currentValue = ""

    def onDivide(self):
        if self.isPending:
            self.calculate()
        self.isPending = True
        self.operation = "divide"
        self.value1 = self.currentValue
        self.txtDisplay.clear()
        self.currentValue = ""

if __name__ == "__main__":
    currentApp = QApplication([])
    currentForm = Calculator()
    currentForm.show()
    currentApp.exec_()