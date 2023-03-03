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
    def __init__(self):
        super().__init__()

        app = QApplication(sys.argv)
        window = QMainWindow()
        container = QWidget()
        window.setWindowTitle("My First App")

        self.cbInput = QComboBox()
        self.cbInput.addItem("One")
        self.cbInput.addItem("Two")
        self.cbInput.addItem("Three")
        self.cbInput.addItem("Four")

        self.cbInput.currentTextChanged.connect(self.setInputChange)

        self.cbOutput = QComboBox()
        self.cbOutput.addItem("One")
        self.cbOutput.addItem("Two")
        self.cbOutput.addItem("Three")
        self.cbOutput.addItem("Four")

        self.cbOutput.currentTextChanged.connect(self.setOutputChange)

        bstart = QPushButton("Start")
        bstop = QPushButton("Stop")

        icons = sorted(
            [attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")]
        )

        btnContainer = QWidget()
        btn = QPushButton("Save")
        btn.setIcon(
            container.style().standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton)
        )

        bstart.clicked.connect(self.startButton)
        bstop.clicked.connect(self.stopButton)

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

        layoutHButton.addWidget(bstart)
        layoutHButton.addWidget(bstop)

        layoutV.addWidget(btn)
        layoutV.addLayout(layoutHCombos)
        layoutV.addLayout(layoutHButton)

        # container.addLoayout(layoutH)
        container.setLayout(layoutV)
        # container.setLayout(layoutH)
        # container.setLayout(layoutV)

        window.setCentralWidget(container)

        window.show()

        app.exec()

    def startButton(self):
        print("start")

    def stopButton(self):
        print("stop")

    def setInputChange(self, s):
        print("Input text: ", s)

    def setOutputChange(self, s):
        print("Output text: ", s)


mc = MainWindow()
