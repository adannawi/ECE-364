# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created: Sun Nov  6 00:00:39 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(422, 256)
        self.centralwidget = QtGui.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.btn9 = QtGui.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(170, 51, 75, 23))
        self.btn9.setObjectName("btn9")
        self.btn6 = QtGui.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.btn6.setObjectName("btn6")
        self.btn1 = QtGui.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(7, 109, 75, 23))
        self.btn1.setObjectName("btn1")
        self.btn5 = QtGui.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(88, 80, 75, 23))
        self.btn5.setObjectName("btn5")
        self.btn2 = QtGui.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(88, 109, 75, 23))
        self.btn2.setObjectName("btn2")
        self.btn7 = QtGui.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(7, 51, 75, 23))
        self.btn7.setObjectName("btn7")
        self.btn8 = QtGui.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(88, 51, 75, 23))
        self.btn8.setObjectName("btn8")
        self.btn4 = QtGui.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(7, 80, 75, 23))
        self.btn4.setObjectName("btn4")
        self.btn3 = QtGui.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(170, 109, 75, 23))
        self.btn3.setObjectName("btn3")
        self.btnDot = QtGui.QPushButton(self.centralwidget)
        self.btnDot.setGeometry(QtCore.QRect(170, 138, 75, 23))
        self.btnDot.setObjectName("btnDot")
        self.btn0 = QtGui.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(7, 138, 155, 23))
        self.btn0.setObjectName("btn0")
        self.btnMultiply = QtGui.QPushButton(self.centralwidget)
        self.btnMultiply.setGeometry(QtCore.QRect(251, 80, 75, 23))
        self.btnMultiply.setObjectName("btnMultiply")
        self.btnMinus = QtGui.QPushButton(self.centralwidget)
        self.btnMinus.setGeometry(QtCore.QRect(251, 109, 75, 23))
        self.btnMinus.setObjectName("btnMinus")
        self.btnPlus = QtGui.QPushButton(self.centralwidget)
        self.btnPlus.setGeometry(QtCore.QRect(251, 138, 75, 23))
        self.btnPlus.setObjectName("btnPlus")
        self.btnDivide = QtGui.QPushButton(self.centralwidget)
        self.btnDivide.setGeometry(QtCore.QRect(251, 51, 75, 23))
        self.btnDivide.setObjectName("btnDivide")
        self.btnEqual = QtGui.QPushButton(self.centralwidget)
        self.btnEqual.setGeometry(QtCore.QRect(338, 109, 75, 52))
        self.btnEqual.setObjectName("btnEqual")
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(338, 51, 75, 52))
        self.btnClear.setObjectName("btnClear")
        self.txtDisplay = QtGui.QLineEdit(self.centralwidget)
        self.txtDisplay.setGeometry(QtCore.QRect(7, 9, 405, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDisplay.setFont(font)
        self.txtDisplay.setInputMask("")
        self.txtDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtDisplay.setObjectName("txtDisplay")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(8, 170, 405, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lblDecimal = QtGui.QLabel(self.groupBox)
        self.lblDecimal.setGeometry(QtCore.QRect(8, 9, 65, 21))
        self.lblDecimal.setScaledContents(False)
        self.lblDecimal.setWordWrap(False)
        self.lblDecimal.setObjectName("lblDecimal")
        self.cboDecimal = QtGui.QComboBox(self.groupBox)
        self.cboDecimal.setGeometry(QtCore.QRect(80, 10, 31, 20))
        self.cboDecimal.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.cboDecimal.setObjectName("cboDecimal")
        self.cboDecimal.addItem("")
        self.cboDecimal.addItem("")
        self.cboDecimal.addItem("")
        self.cboDecimal.addItem("")
        self.cboDecimal.addItem("")
        self.cboDecimal.addItem("")
        self.chkSeparator = QtGui.QCheckBox(self.groupBox)
        self.chkSeparator.setGeometry(QtCore.QRect(230, 10, 171, 21))
        self.chkSeparator.setChecked(True)
        self.chkSeparator.setObjectName("chkSeparator")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        self.cboDecimal.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QtGui.QApplication.translate("Calculator", "Basic Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.btn9.setText(QtGui.QApplication.translate("Calculator", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.btn6.setText(QtGui.QApplication.translate("Calculator", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.btn1.setText(QtGui.QApplication.translate("Calculator", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.btn5.setText(QtGui.QApplication.translate("Calculator", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.btn2.setText(QtGui.QApplication.translate("Calculator", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.btn7.setText(QtGui.QApplication.translate("Calculator", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.btn8.setText(QtGui.QApplication.translate("Calculator", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.btn4.setText(QtGui.QApplication.translate("Calculator", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.btn3.setText(QtGui.QApplication.translate("Calculator", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDot.setText(QtGui.QApplication.translate("Calculator", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.btn0.setText(QtGui.QApplication.translate("Calculator", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMultiply.setText(QtGui.QApplication.translate("Calculator", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMinus.setText(QtGui.QApplication.translate("Calculator", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPlus.setText(QtGui.QApplication.translate("Calculator", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDivide.setText(QtGui.QApplication.translate("Calculator", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEqual.setText(QtGui.QApplication.translate("Calculator", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("Calculator", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.txtDisplay.setText(QtGui.QApplication.translate("Calculator", "0.", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDecimal.setText(QtGui.QApplication.translate("Calculator", "Decimal Digits", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDecimal.setItemText(0, QtGui.QApplication.translate("Calculator", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDecimal.setItemText(1, QtGui.QApplication.translate("Calculator", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDecimal.setItemText(2, QtGui.QApplication.translate("Calculator", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDecimal.setItemText(3, QtGui.QApplication.translate("Calculator", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDecimal.setItemText(4, QtGui.QApplication.translate("Calculator", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.cboDecimal.setItemText(5, QtGui.QApplication.translate("Calculator", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.chkSeparator.setText(QtGui.QApplication.translate("Calculator", "Display Thousands\' Separator", None, QtGui.QApplication.UnicodeUTF8))

