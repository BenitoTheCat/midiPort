# https://stackoverflow.com/questions/71808759/reduce-latency-in-midi-gui
from MainWindow import MainWindow
from DataJson import DataJson
from MidiClass import MidiClass
from threading import Thread
import sys
import json


class MainClass:
    def __init__(self):
        super().__init__()

        # Midi init

        self.midi = MidiClass()

        self.linput = self.midi.getInportNames()
        self.loutput = self.midi.getOutportNames()

        # Settings init

        self.dj = DataJson()

        self.setting = self.dj.getSetting()
        self.input = self.dj.getInput()
        self.output = self.dj.getOutput()

        print("MainClass: ", self.setting, self.input, self.output)

        # Thread init
        self.running = False
        self.thread = None

        # Gui init

        self.app = MainWindow(self.linput, self.loutput)

        self.app.getStartButton().clicked.connect(self.startButton)
        self.app.getStopButton().clicked.connect(self.stopButton)
        self.app.getSaveButton().clicked.connect(self.saveButton)

        self.app.getComboInput().currentTextChanged.connect(self.setInputChange)
        self.app.getComboOutput().currentTextChanged.connect(self.setOutputChange)

        # Set settings
        self.setSetting(self.linput, self.input, self.loutput, self.output)

        self.app.getApp().exec()

    def createThread(self):
        return Thread(target=self.startHost)

    def startHost(self):
        self.midi.startMidiHost()

    def startButton(self):
        print("Main start")
        if self.running:
            return "Already running"

        self.running = True
        self.thread = self.createThread()
        self.thread.daemon = True
        self.thread.start()
        return "OK"

    def stopButton(self):
        print("Main stop")
        if self.running:
            self.running = False
            self.thread.join()
            return "OK"
        return "Not running"

    def saveButton(self):
        self.setting = {"input": self.input, "output": self.output}
        self.dj.setSetting(json.dumps(self.setting))
        print("Main save")

    def setInputChange(self, s):
        self.input = s
        self.midi.setInport(s)
        print("Main Input text: ", s)

    def setOutputChange(self, s):
        self.output = s
        self.midi.setOutport(s)
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

    def setSetting(self, linput, input, loutput, output):
        if self.checkInput(linput, input):
            self.app.getComboInput().setCurrentText(input)
        else:
            self.input = self.app.getComboInput().currentText()

        if self.checkOutput(loutput, output):
            self.app.getComboOutput().setCurrentText(output)
        else:
            self.output = self.app.getComboOutput().currentText()

        self.setting = {"input": self.input, "output": self.output}
        self.midi.setMidiHost(self.input, self.output)


print("mainClass.py")
mc = MainClass()
