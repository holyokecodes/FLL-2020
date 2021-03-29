from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# M09 - Tires, M03 - Slide, M08 - Boccia, M04 - Bench

#Facing toward Bench, back of robot on the wall, left wheel's edge is on the edge of the box.

def comboThree(robot, ev3, library, medium_motor, sensor_l):
    
    
    # and take it.
    
    # robot.straight(library.inch_to_mm(3)) 
    # robot.turn(10)
    # robot.straight(library.inch_to_mm(10))
    # robot.turn(-140)
    #robot.straight(250)
    #robot.straight(-250)
    
    # Go to bench,
    robot.settings(turn_rate=57)
    robot.turn(-45)
    robot.straight(library.inch_to_mm(26))
    robot.turn(-120)

    # Knock it over
    robot.straight(library.inch_to_mm(3))
    robot.straight(library.inch_to_mm(-2))

    # Go to position where the backrest can be obtained

    #Move around the bench
    robot.drive(100, -40)
    wait(1400)
    robot.stop(Stop.BRAKE)
    
    #Drive the robot aside of the backrest
    robot.straight(library.inch_to_mm(1))
    
    #Align parellel to backrest
    robot.drive(110, 38.3)
    wait(1500)
    robot.stop(Stop.BRAKE)

    #Move tines even with backrest
    robot.straight(library.inch_to_mm(5.5))
    robot.stop(Stop.BRAKE)
    robot.settings(turn_rate=50)
    robot.turn(40)

    #Throw the backrest across the room somehow
    medium_motor.run_time(speed=1000, time=500)
    wait(2000)
    #robot.turn(-60)
    
    #Drop the cubes
    #robot.straight(library.inch_to_mm(-2))
    medium_motor.run_time(speed=-1000, time=650)
    
    #Go to home'
    robot.turn(-85)
    robot.straight(library.inch_to_mm(20))
    

'''
    #Drives all the way toward the bench.
    #robot.straight(library.inch_to_mm(7))
    robot.stop()
    #robot.turn(20)
    medium_motor.run_time(speed=500, time=2000)
    # medium_motor.run_time(speed=-10000, time=400)
    robot.turn(-35)
    robot.straight(library.inch_to_mm(-6.5))
    medium_motor.run_time(speed=-750, time=750)
    #medium_motor.run_time(speed=750, time=7500)
    #robot.driv
'''
