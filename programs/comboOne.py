from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# M11 - Treadmill, M12 - Row Machine, M13 - Weight Machine

def comboOne(robot, ev3, library):
    #ev3.speaker.say("You pressed down, this button is not supported. DDDDDDDDDD")
    ## Use Library for line following to get to treadmill? Line follow to get back for sure
    robot.straight(library.inch_to_mm(8.5))
    robot.turn(-20)
    sensor_stop = ColorSensor(Port.S1)
    library.line_follow_for_distance(p=1, distance=library.inch_to_mm(48.4645), sensor_lf=sensor_stop)
    ##ev3.speaker.say("That was " + str(library.mm_to_inch(robot.distance())) + " Inches")
    robot.turn(180)
    robot.straight(library.inch_to_mm(-12))
    robot.settings(straight_speed=600)
    robot.straight(library.inch_to_mm(-42))
    robot.settings(straight_speed=150)

    robot.straight(library.inch_to_mm(12))
    library.line_follow_for_distance(p=1, distance=library.inch_to_mm(35), sensor_lf=sensor_stop)
    robot.settings(straight_speed=600)
    robot.straight(library.inch_to_mm(42))
    pass