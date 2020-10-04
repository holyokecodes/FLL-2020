from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# M02 - Step Counter, M06 - Pull-Up Bar, M07 - Robot Dance, M10 - Cell Phone

def comboFour(robot, ev3, library):
    robot.straight(600)
    ev3.speaker.beep()
    robot.stop()

    robot.settings(straight_speed=45)
    robot.straight(250)
    robot.straight(-100)
    robot.turn(90)
    robot.straight(60)
    robot.stop()
    robot.settings(straight_speed=750)
    robot.straight(-630)
    robot.turn(-55) 
    robot.straight(-360)
    robot.turn(-1800)