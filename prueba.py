import sys
import time
import threading
from threading import Thread

from PySide6.QtCore import *
from PySide6.QtGui import *
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


def worker():
    global running
    while running:
        # I am handling connections here that MUST be in continual while loop
        print("loop", time.localtime())
        time.sleep(0.1)


def create_thread():
    return Thread(target=worker)


thread = create_thread()


def startButton():
    print("Main start")
    global running
    running = True

    global thread
    thread = create_thread()
    thread.daemon = True
    thread.start()
    # self.midi.startMidiHost()


def stopButton():
    print("Main stop")
    global running
    running = False

    global thread
    thread.join()


qt_app = QApplication(sys.argv)
window = QMainWindow()
label = QLabel("Hello, loop!")

container = QWidget()

lay = QVBoxLayout()

bStart = QPushButton("Start")
bStop = QPushButton("Stop")


bStart.clicked.connect(startButton)
bStop.clicked.connect(stopButton)

lay.addWidget(label)
lay.addWidget(bStart)
lay.addWidget(bStop)

container.setLayout(lay)
window.setCentralWidget(container)

window.show()

running = True  # only set to False when user is done with app in the real code.


thread.daemon = True
thread.start()

qt_app.exec()
