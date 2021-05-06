from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, SoundFile, ImageFile


# Treadmill, Rowing Machine, Weight Machine, Slide

def comboOne(robot, ev3, library, left_motor, medium_motor, buttons):
    print(buttons, sep=' ', end='\n')
    robot.straight(library.inch_to_mm(10.25))
    # get to line
    robot.turn(-20)
    #set color sensor vars
    sensor_stop = ColorSensor(Port.S1) 
    #line follow
    library.line_follow_for_distance(p=1, distance=library.inch_to_mm(20.5), sensor_lf=sensor_stop, DRIVE_SPEED=150) #line follow to treadmill
    ev3.speaker.beep()
    robot.turn(-70) # Dump the
    robot.straight(library.inch_to_mm(2))
    robot.straight(library.inch_to_mm(-2))
    robot.turn(70) #  Inno Project
    library.line_follow_for_distance(p=1, distance=library.inch_to_mm(29), sensor_lf=sensor_stop, DRIVE_SPEED=150) #line follow to treadmill
    wait(250)
    #turn to back onto treadmill
    robot.turn(173)
    #back onto treamill
    robot.straight(library.inch_to_mm(-12)) 
    robot.stop()
    #turn left motor to do the treamill
    left_motor.run_target(speed = -600, target_angle=840) 
    #get off the treadmill
    robot.straight(library.inch_to_mm(14)) 
    # Drive to rowing machine
    robot.turn(90)
    # use the wall to make sure we are straight
    robot.straight(library.inch_to_mm(-10))
    robot.straight(library.inch_to_mm(16.5))
    # turn to face the rowing machine

    robot.turn(110) #if it breaks, set this to 114

    # arrive at rowing machine
    robot.straight(library.inch_to_mm(1.6))
    # lower attachment to get the tire
    medium_motor.run_time(speed=1000, time=2400)
    # backup to drag the tire to the target zone
    robot.straight(-132)
    robot.turn(20)
    # raise the attachment
    medium_motor.run_time(speed=-1000, time=2500)
    robot.straight(library.inch_to_mm(5))
    # Go to weight machine
    

  
    
    robot.turn(-95)
    robot.straight(library.inch_to_mm(13))
    robot.turn(-20) # it was -40, and before that it was at -33
    robot.straight(library.inch_to_mm(4))
    
    medium_motor.run_time(speed=1000, time=2750, wait=True)
    #robot.drive(0,5)
    robot.stop()
    medium_motor.run_time(speed=-1000, time=1500)
    robot.straight(library.inch_to_mm(-8))
    
    robot.drive(70,-70)
    robot.stop()
    library.line_follow_for_distance(p=1, distance=library.inch_to_mm(40), sensor_lf=-2)
    robot.straight(library.inch_to_mm(2.5))
    medium_motor.run_time(-1000, 1000, wait=False)
    robot.turn(51)
    robot.stop()
    robot.settings(straight_speed=800)
    robot.straight(library.inch_to_mm(44))

    # robot.settings(straight_speed=600)
    # robot.straight(library.inch_to_mm(36))
    # 
    # robot.straight(library.inch_to_mm(8.75))
    # 
    # robot.stop()
    # 
    # robot.settings(straight_speed=33)
    # medium_motor.run_time(speed=200, time=2000, wait=False)
    # robot.straight(library.inch_to_mm(3.5))
    # robot.stop()
    # robot.settings(straight_speed=100)
    # robot.straight(library.inch_to_mm(-1.6))
    # robot.straight(library.inch_to_mm(2.25))