# -*- coding: utf-8 -*-
"""Serial Connection to a Board"""

from serial import Serial
from serial.tools.list_ports import comports

CPSAMD_PID = 516
CPSAMD_VID = 3368
BAUDRATE = 115200
PARITY = 'N'


def find_board():
    """Find port where first board is connected."""
    for port in comports():
        if port.vid == CPSAMD_VID and port.pid == CPSAMD_PID:
            return port.device


def connect():
    """Connect to a pySerial Serial object.

    If you do not see the REPL hit `enter` a few times. Control-A or Home
    sends you to beginning of line. Control-E or End to the end of the line.

    ESP8266 REPL prompt is `>>>`

    SAMD21 REPL prompt is `>>>`

    There are four other control commands:

    Ctrl-A on a blank line will enter raw REPL mode. This is like a permanent
    paste mode, except that characters are not echoed back.

    Ctrl-B on a blank like goes to normal REPL mode.

    Ctrl-C cancels any input, or interrupts the currently running code.

    Ctrl-D on a blank line will do a soft reset.

    Note that ctrl-A and ctrl-D do not work with WebREPL.

    """
    #s = Serial(find_circuitpython_board(), BAUDRATE, parity=PARITY)
    # Hardcoded current device
    s = Serial('/dev/tty.usbmodem1421', BAUDRATE, parity=PARITY)
    s.write(b'\x03\x01')  # Ctrl-C: interrupt, Ctrl-A: switch to raw REPL
    s.read_until(b'raw REPL')
    s.read_until(b'\r\n>')  # Wait for prompt
    return s
