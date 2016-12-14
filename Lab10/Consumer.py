import sys

from PySide.QtGui import *
from BasicUI import *
import re


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.clearButton.clicked.connect(self.clearGUI)
        self.firstNameLineEdit.textChanged.connect(self.updateField)
        self.lastNameLineEdit.textChanged.connect(self.updateField)
        self.addressLineEdit.textChanged.connect(self.updateField)
        self.cityLineEdit.textChanged.connect(self.updateField)
        self.stateLineEdit.textChanged.connect(self.updateField)
        self.zipLineEdit.textChanged.connect(self.updateField)
        self.emailLineEdit.textChanged.connect(self.updateField)
        self.saveToTargetButton.clicked.connect(self.validateSave)
        self.loadButton.clicked.connect(self.loadData)

    def validateSave(self):
        err = 0
        if self.stateLineEdit.text() == "" or self.firstNameLineEdit.text() == "" or self.lastNameLineEdit.text() == "" or self.addressLineEdit.text() == "" or self.zipLineEdit.text() == "" or self.cityLineEdit.text() == "" or self.emailLineEdit.text() == "":
            self.errorInfoLabel.setText("All fields must be populated!")
        elif self.stateLineEdit.text() not in self.states:
            self.errorInfoLabel.setText("ERROR: State not valid!")
        elif re.search(r"\w+@\w+\.\w+", self.emailLineEdit.text()) == None:
            print("hi!")
            self.errorInfoLabel.setText("Invalid email")
        elif len(self.zipLineEdit.text()) is not 5:
            self.errorInfoLabel.setText("ERROR: Zip code not valid!")
        elif self.checkZipcode():
            self.errorInfoLabel.setText("Error: Zip code has invalid characters!")
        else:
            self.errorInfoLabel.clear()
            s = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<user>\n\t<FirstName>{}</FirstName>\n\t<LastName>{}</LastName>\n\t<Address>{}</Address>\n\t<City>{}</City>\n\t<State>{}</State>\n\t<ZIP>{}</ZIP>\n\t<Email>{}</Email>\n</user>".format(self.firstNameLineEdit.text(), self.lastNameLineEdit.text(), self.addressLineEdit.text(), self.cityLineEdit.text(), self.stateLineEdit.text(), self.zipLineEdit.text(), self.emailLineEdit.text())
            print(s)
            with open("target.xml", "w") as saveFile:
                saveFile.write(s)

    def checkZipcode(self):
        if (len(self.zipLineEdit.text()) is not 5):
            return 1
        for char in self.zipLineEdit.text():
              if char not in ["1","2","3","4","5","6","7","8","9","0"]:
                    return 1
        return 0

    def updateField(self):
        self.saveToTargetButton.setEnabled(1)
        self.loadButton.setEnabled(0)
    def clearGUI(self):
        self.firstNameLineEdit.clear()
        self.lastNameLineEdit.clear()
        self.addressLineEdit.clear()
        self.cityLineEdit.clear()
        self.stateLineEdit.clear()
        self.zipLineEdit.clear()
        self.emailLineEdit.clear()
        self.saveToTargetButton.setEnabled(0)
        self.loadButton.setEnabled(1)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        with open(filePath) as xmlFile:
            allLines = xmlFile.read()
            parameters = re.findall(r"\s*<\w+>(.*)</\w+>\s*", allLines)
            print(parameters)
            self.firstNameLineEdit.setText(parameters[0])
            self.lastNameLineEdit.setText(parameters[1])
            self.addressLineEdit.setText(parameters[2])
            self.cityLineEdit.setText(parameters[3])
            self.stateLineEdit.setText(parameters[4])
            self.zipLineEdit.setText(parameters[5])
            self.emailLineEdit.setText(parameters[6])
            self.updateField()


    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()
    currentForm.show()
    currentApp.exec_()
