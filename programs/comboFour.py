from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# M02 - Step Counter, M06 - Pull-Up Bar, M07 - Robot Dance, M10 - Cell Phone

def comboFour(robot, ev3, library, medium_motor):

    # head towards the step counter
    robot.turn(3)
    robot.straight(802)
    ev3.speaker.beep()
    #push it
    # robot.turn(-6)
    robot.stop()
    robot.settings(straight_speed=30)
    robot.straight(280)
    robot.stop()
    #head towards dance
    robot.settings(straight_speed=200)
    robot.straight(-100)
    robot.turn(-90)
    robot.straight(-100)
    robot.stop()
    robot.settings(straight_speed=550)
    robot.straight(40)
    robot.turn(-25) 
    robot.straight(50)
    robot.turn(25)
    medium_motor.run_time(100, 1000)
    robot.turn(135)
    robot.straight(-inch_to_mm(7))