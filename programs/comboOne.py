from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile


# Treadmill, Rowing Machine, Weight Machine, Slide

def comboOne(robot, ev3, library, left_motor, medium_motor, buttons, sensor_b):
    print(buttons, sep=' ', end='\n')
    robot.straight(library.inch_to_mm(8.5))
    # get to line
    robot.turn(-20)
    #set color sensor vars
    sensor_stop = ColorSensor(Port.S1) 
    #line follow
    library.line_follow_for_distance(p=1, distance=library.inch_to_mm(48.5), sensor_lf=sensor_stop, DRIVE_SPEED=150) #line follow to treadmill
    wait(250)
    #turn to back onto treadmill
    robot.turn(172)
    #back onto treamill
    robot.straight(library.inch_to_mm(-12)) 
    robot.stop()
    #turn left motor to do the treamill
    left_motor.run_target(speed = 600, target_angle=840) 
    #get off the treadmill
    robot.straight(library.inch_to_mm(12)) 
    # Drive to rowing machine
    robot.turn(90)
    # use the wall to make sure we are straight
    robot.straight(library.inch_to_mm(-4.5))
    robot.straight(library.inch_to_mm(10))
    # turn to face the rowing machine
    robot.turn(68)
    # arrive at rowing machine
    robot.straight(40)
    # lower attachment to get the tire
    medium_motor.run_time(speed=-150, time=3500)
    medium_motor.run_time(speed=-150, time=2000)
    # backup to drag the tire to the target zone
    robot.straight(-132)
    robot.turn(-6)
    # raise the attachment
    medium_motor.run_time(speed=200, time=5000)
    # Go to weight machine
    medium_motor.run_time(speed=400, time=500, wait=False)
    robot.turn(-67)
    robot.straight(420)
    # Lift weight
    medium_motor.run_time(speed=-200, time=7000)
    medium_motor.run_time(speed=400, time=7000)
    """
    robot.turn(-90)
    robot.straight(library.inch_to_mm(2))
    
    
    
    robot.turn(-90)
    
    
    robot.turn(115)
    #go home
    
    robot.straight(library.inch_to_mm(10.5))
    robot.turn(90)
    library.line_follow_for_distance(p=-1, distance=library.inch_to_mm(37))
    robot.settings(straight_speed=600)
    robot.straight(library.inch_to_mm(36))
    
    robot.straight(library.inch_to_mm(8.75))

    robot.stop()
    
    robot.settings(straight_speed=33)
    medium_motor.run_time(speed=200, time=2000, wait=False)
    robot.straight(library.inch_to_mm(3.5))
    robot.stop()
    robot.settings(straight_speed=100)
    robot.straight(library.inch_to_mm(-1.6))
    robot.straight(library.inch_to_mm(2.25))
    """