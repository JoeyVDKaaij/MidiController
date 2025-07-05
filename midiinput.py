import rtmidi
from PyQt6.QtCore import QThread
import sys
import threading

class MidiInput(QThread):
    def __init__(self, devid, parent=None):
        QThread.__init__(self, parent)
        self.device = rtmidi.RtMidiIn()
        self.device.openPort(devid)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            msg = self.device.getMessage(250)
            if msg:
                self.msg = msg
                self.emit(SIGNAL('message(PyObject *)'), self.msg)
                self.emit(SIGNAL('message()')

midi = MidiInput(1)
def slotMessage(msg):
   print msg
QObject.connect(midi, SIGNAL('message(PyObject *)'), slotMessage)