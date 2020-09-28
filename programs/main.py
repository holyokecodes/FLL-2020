#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

#import the library
from library import FUNCTION_LIBRARY

#import the combos
from comboOne import *
from comboTwo import *
from comboThree import *
from comboFour import *

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# For more information:
# https://pybricks.github.io/ev3-micropython/

# Create your objects here.
ev3 = EV3Brick()
#motorA = Motor(Port.A)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

sensor_b = ColorSensor(Port.S2)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# init the library
library = FUNCTION_LIBRARY(robot, ev3, left_motor, right_motor, sensor_b)

ev3.screen.load_image( Image('../images/FLLButtons.png') )

while True:
    if Button.LEFT in ev3.buttons.pressed():
        comboOne(robot, ev3, library)
    if Button.RIGHT in ev3.buttons.pressed():
        comboTwo(robot, ev3, library)
    if Button.UP in ev3.buttons.pressed():
        comboFour(robot, ev3, library)
    if Button.DOWN in ev3.buttons.pressed():
        comboThree(robot, ev3, library)

#hello there