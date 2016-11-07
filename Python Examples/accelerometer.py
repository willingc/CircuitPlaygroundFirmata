#!/usr/bin/python

"""
accelerometer.py
----------------

A basic accelerometer example


Example
-------

python accelerometer.py /dev/ttyACM0

"""

import sys
import time

# Import CircuitPlayground class from `circuitplayground.py` in the same directory.
from circuitplayground import CircuitPlayground


# Check if command specifies a serial port
if len(sys.argv) != 2:
    print('ERROR: Must specify the serial port as command line parameter.')
    sys.exit(-1)
port = sys.argv[1]

# Connect to Circuit Playground board on specified serial port.
board = CircuitPlayground(port)


def accel_data(x, y, z):
    """Print accelerometer data nicely """
    print('Received accelerometer data!')
    print('X = {0}'.format(x))
    print('Y = {0}'.format(y))
    print('Z = {0}'.format(z))


print('Printing accelerometer data (Ctrl-C to quit)...')
# Request and read accelerometer data. Sleep for 2 seconds betweem reads."
while True:
    board.read_accel(accel_data)
    time.sleep(2.0)

# Close Circuit Playground board connection when done.
board.close()
