import mido
import time
from collections import deque
import sys


class MidiClass:
    def __init__(self):
        super().__init__()

        self.inportNames = mido.get_input_names()
        self.outportNames = mido.get_output_names()

        self.inport = None
        self.outport = None

        self.msglog = deque()
        self.echo_delay = 0

    def setInport(self, name):
        self.inport = mido.open_input(name)

    def setOutport(self, name):
        self.outport = mido.open_output(name)

    def getInportNames(self):
        return self.inportNames

    def getOutportNames(self):
        return self.outportNames

    def setMidiHost(self, inport, outport):
        self.inport = mido.open_input(inport)
        self.outport = mido.open_output(outport)

    def startMidiHost(self):
        while True:
            for msg in self.inport.iter_pending():
                # msg = inport.receive()
                if msg.type != "clock":
                    print(msg)
                    self.msglog.append(
                        {"msg": msg, "due": time.time() + self.echo_delay}
                    )
            while len(self.msglog) > 0 and self.msglog[0]["due"] <= time.time():
                self.outport.send(self.msglog.popleft()["msg"])

            time.sleep(0.01)


# print(mido.get_output_names())  # To list the output ports
# print(mido.get_input_names())  # To list the input ports

# inport = mido.open_input("FBV Shortboard Mk II 1")
# outport = mido.open_output("2- Quad Cortex MIDI OUT 1")

# msglog = deque()
# echo_delay = 0


# while True:
#     for msg in inport.iter_pending():
#         # msg = inport.receive()
#         if msg.type != "clock":
#             print(msg)
#             msglog.append({"msg": msg, "due": time.time() + echo_delay})
#     while len(msglog) > 0 and msglog[0]["due"] <= time.time():
#         outport.send(msglog.popleft()["msg"])
