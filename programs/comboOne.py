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
    robot.turn(-20)# get to line
    sensor_stop = ColorSensor(Port.S1) #set color sensor vars
    library.line_follow_for_distance(p=1, distance=library.inch_to_mm(48.5), sensor_lf=sensor_stop, DRIVE_SPEED=150) #line follow to treadmill
    wait(250)
    robot.turn(170)
    #turn 180 to back onto treadmill
    
    robot.straight(library.inch_to_mm(-12)) #back onto treamill
    
    robot.stop()
    
    left_motor.run_target(speed = 600, target_angle=840) #turn left motor to do the treamill
    robot.straight(library.inch_to_mm(12)) #get off the treadmill
    
    # Drive to rowing machine
    robot.turn(90)
    # use the wall to make sure we are straight
    robot.straight(library.inch_to_mm(-4.5))
    robot.straight(library.inch_to_mm(17.5))
    # turn to face the rowing machine
    robot.turn(97)
    # arrive at rowing machine
    robot.straight(library.inch_to_mm(1))
    # lower attachment to get the tire
    medium_motor.run_time(speed=-150, time=4000)
    robot.straight(-130)
    # raise the attachment
    robot.turn(2)
    medium_motor.run_time(speed=200, time=5000)
    """    # Go to weight machine
    robot.turn(-65)
    robot.straight(library.inch_to_mm(14.75))
    # Lift weight
    medium_motor.run_time(speed=-200, time=6000)
    
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