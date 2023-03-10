#!/usr/bin/env python
#
# 
# Hardware:
#
# Results:

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

try:
    try:
        BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A)) # reset encoder A
        BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D)) # reset encoder D
    except IOError as error:
        print(error)
    
    # BP.set_motor_power(BP.PORT_D, BP.MOTOR_FLOAT)                          # float motor D
    BP.set_motor_limits(BP.PORT_A, 50)                                     # optionally set a power limit
    BP.set_motor_limits(BP.PORT_D, 50)                                     # optionally set a power limit
    while True:
        target = 180 #dps
        robot_width = 20
        
        BP.set_motor_dps(BP.PORT_A, target)             # set the target speed for motor A in Degrees Per Second
        BP.set_motor_dps(BP.PORT_D, target)
        
        t = 4.24 # time to run a side
        t2 = 3.3 # time to turn
        
        time.sleep(t)
        
        BP.set_motor_dps(BP.PORT_A, 0)             # set the target speed for motor A in Degrees Per Second
        
        time.sleep(t2)
        
        print(("Motor A Target Degrees Per Second: %d" % target), "  Motor A Status: ", BP.get_motor_status(BP.PORT_A))
        
        time.sleep(0.02)

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.

