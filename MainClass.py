from MainWindow import MainWindow
from DataJson import DataJson
import sys
import json


class MainClass:
    def __init__(self):
        super().__init__()

        # Midi init

        self.list = ["One", "Two", "Three", "Four"]

        # Settings init

        self.dj = DataJson()

        self.setting = self.dj.getSetting()
        self.input = self.dj.getInput()
        self.output = self.dj.getOutput()

        print("MainClass: ", self.setting, self.input, self.output)

        # Gui init

        self.app = MainWindow(self.list)

        self.app.getStartButton().clicked.connect(self.startButton)
        self.app.getStopButton().clicked.connect(self.stopButton)
        self.app.getSaveButton().clicked.connect(self.saveButton)

        self.app.getComboInput().currentTextChanged.connect(self.setInputChange)
        self.app.getComboOutput().currentTextChanged.connect(self.setOutputChange)

        # Set settings
        self.setSetting(self.list, self.input, self.output)

        self.app.getApp().exec()

    def startButton(self):
        print("Main start")

    def stopButton(self):
        print("Main stop")

    def saveButton(self):
        self.setting = {"input": self.input, "output": self.output}
        self.dj.setSetting(json.dumps(self.setting))
        print("Main save")

    def setInputChange(self, s):
        self.input = s
        print("Main Input text: ", s)

    def setOutputChange(self, s):
        self.output = s
        print("Main Output text: ", s)

    # check if input is in list
    def checkInput(self, list, input):
        for n in list:
            if n == input:
                return True
        return False

    # check if output is in list
    def checkOutput(self, list, output):
        for n in list:
            if n == output:
                return True
        return False

    def setSetting(self, list, input, output):
        if self.checkInput(list, input):
            self.app.getComboInput().setCurrentText(input)

        if self.checkOutput(list, output):
            self.app.getComboOutput().setCurrentText(output)


print("mainClass.py")
mc = MainClass()
