import rtmidi
from rtmidi import MidiMessage
midiin = rtmidi.RtMidiIn()
midiout = rtmidi.RtMidiOut()
midimessage = MidiMessage()

def print_message(midi):
    if midi.isNoteOn():
        print('ON: ', midi.getMidiNoteName(midi.getNoteNumber()), midi.getVelocity())
    elif midi.isNoteOff():
        print('OFF:', midi.getMidiNoteName(midi.getNoteNumber()))
    elif midi.isController():
        print('CONTROLLER', midi.getControllerNumber(), midi.getControllerValue())

outports = range(midiout.getPortCount())
if outports:
    for i in outports:
        print(midiout.getPortName(i))
    print("Opening port 0!")
    midiout.openPort(0)
    note = 60  # Change this to the pad you want to light up
    color = 5  # Varies based on the Launchpad color palette
    velocity = color  # Launchpad uses velocity for colors
    m = midimessage.noteOn(100, 11, 77)
    print_message(m)
    midiout.sendMessage(m)
    # while True:
    #     print_message(m)
    # while True:
    #     midiout.sendMessage(m)

ports = range(midiin.getPortCount())
if ports:
    for i in ports:
        print(midiin.getPortName(i))
    print("Opening port 0!")
    midiin.openPort(0)
    while True:
        m = midiin.getMessage() # some timeout in ms
        if m:
            print_message(m)
            print(m.getNoteNumber())
else:
    print('NO MIDI INPUT PORTS!')