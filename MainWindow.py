from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow,
    QComboBox,
    QComboBox,
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QStyle,
)
import sys
import json


class MainWindow:
    def __init__(self, linput=["1", "2", "3", "4"], loutput=["1", "2", "3", "4"]):
        super().__init__()

        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.container = QWidget()
        self.window.setWindowTitle("midiPort")

        self.cbInput = self.setCombo(linput)

        self.cbOutput = self.setCombo(loutput)

        self.bStart = QPushButton("Start")
        self.bStop = QPushButton("Stop")

        self.bSave = QPushButton("Save")
        self.bSave.setIcon(
            self.container.style().standardIcon(
                QStyle.StandardPixmap.SP_DialogSaveButton
            )
        )

        layoutVInput = QVBoxLayout()
        layoutVOutput = QVBoxLayout()
        layoutHCombos = QHBoxLayout()
        layoutHButton = QHBoxLayout()
        layoutV = QVBoxLayout()

        linput = QLabel("Input")
        loutput = QLabel("Output")

        layoutVInput.addWidget(linput)
        layoutVInput.addWidget(self.cbInput)

        layoutVOutput.addWidget(loutput)
        layoutVOutput.addWidget(self.cbOutput)

        layoutHCombos.addLayout(layoutVInput)
        layoutHCombos.addLayout(layoutVOutput)

        layoutHButton.addWidget(self.bStart)
        layoutHButton.addWidget(self.bStop)

        layoutV.addWidget(self.bSave)
        layoutV.addLayout(layoutHCombos)
        layoutV.addLayout(layoutHButton)

        self.container.setLayout(layoutV)

        self.window.setCentralWidget(self.container)

        self.window.show()

    def setCombo(self, list):
        combo = QComboBox()
        for n in list:
            combo.addItem(n)
        return combo

    # function return self app
    def getApp(self):
        return self.app

    # function return self cbInput
    def getComboInput(self):
        return self.cbInput

    # function return self cbOutput
    def getComboOutput(self):
        return self.cbOutput

    # function return self bSave
    def getSaveButton(self):
        return self.bSave

    # function return self bStart
    def getStartButton(self):
        return self.bStart

    # function return self bStop
    def getStopButton(self):
        return self.bStop
