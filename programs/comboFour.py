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
    robot.stop()
    robot.settings(straight_speed=550)
    robot.turn(3)
    robot.straight(830)
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
    # robot.turn(-90)
    robot.straight(-10) # Do A
    robot.turn(-40)     # Three
    robot.straight(40)  # Point
    robot.turn(-40)     # Turn
    robot.stop()
    robot.settings(straight_speed=550)
    robot.straight(library.inch_to_mm(22))
    robot.turn(-45)
    robot.straight(library.inch_to_mm(10.2))
    robot.turn(47)
    # ev3.say("Mooooove!")
    robot.straight(25.4)
    medium_motor.run_time(-200, 1000)
    ev3.speaker.beep()
    robot.turn(135)
    ev3.speaker.beep()
    robot.straight(library.inch_to_mm(-7))
    ev3.speaker.beep()
    while True:
        robot.turn(25)
        robot.turn(-25)