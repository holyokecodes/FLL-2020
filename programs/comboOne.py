from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile

def comboOne(robot, ev3, library, left_motor, medium_motor, buttons):
    print(buttons, sep=' ', end='\n')
    robot.straight(library.inch_to_mm(8.5))
    robot.turn(-20)# get to line
    sensor_stop = ColorSensor(Port.S1) #set color sensor vars
    library.line_follow_for_distance(p=1, distance=library.inch_to_mm(48.5), sensor_lf=sensor_stop, DRIVE_SPEED=150) #line follow to treadmill
    wait(250)
    robot.turn(180) #turn 180 to back onto treadmill
    robot.straight(library.inch_to_mm(-12)) #back onto treamill
    robot.stop()
    left_motor.run_target(speed = 600, target_angle=840) #turn left motor to do the treamill
    robot.straight(library.inch_to_mm(12)) #get off the treadmill
    # Drive to rowing machine
    robot.turn(-87)
    robot.straight(library.inch_to_mm(-11))
    robot.turn(-94)
    # arrive at rowing machine
    robot.straight(library.inch_to_mm(3.25))
    medium_motor.run_time(speed=-150, time=4000)
    robot.straight(-120)
    robot.turn(-10)
    medium_motor.run_time(speed=200, time=5000)
    robot.turn(-65)
    robot.straight(library.inch_to_mm(14.75))
    medium_motor.run_time(speed=-200, time=6000)
    """
    robot.turn(-90)
    robot.straight(library.inch_to_mm(2))
    
    
    
    robot.turn(-90)
    
    # arrive at weight machine
    robot.turn(115)
    #go home
    
    robot.straight(library.inch_to_mm(10.5))
    robot.turn(90)
    library.line_follow_for_distance(p=-1, distance=library.inch_to_mm(37))
    robot.settings(straight_speed=600)
    robot.straight(library.inch_to_mm(36))
    
    robot.straight(library.inch_to_mm(8.75))
    """