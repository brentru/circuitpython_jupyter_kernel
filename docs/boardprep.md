
# Board Preparation

Before you start using the CircuitPython_Kernel, you'll need a board running CircuitPython. If you're not sure if
the board plugged into your computer is running CircuitPython, check your file explorer for a drive named `CIRCUITPY`

This kernel supports all Adafruit CircuitPython boards (SAMD21/SAMD51).

### Installing CircuitPython Firmware

- Download the [CircuitPython Firmware (.uf2 file) from the CircuitPython Repo](https://github.com/adafruit/circuitpython/releases)
- Plug in board and double click the **reset** button to enter bootloader mode.
- Drag and drop the \*.uf2 CircuitPython file to the USB drive.
- If you see the `CIRCUITPY` as the new name of the USB drive, you're ready to go.

### Access the REPL

Use `screen` program:

    screen <device> 115200


## ampy

- Install ampy `python3 -m pip install adafruit-ampy`
- To get options for listing files and moving files: `ampy --help`
