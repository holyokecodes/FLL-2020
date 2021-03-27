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
    
    # settings(turn_acceleration)
    # Go to bench,
    # Run it over,
    # Go to position where bucket can obtain the top piece of the bench,
    # and take it.
    
    # robot.straight(library.inch_to_mm(3)) 
    # robot.turn(10)
    # robot.straight(library.inch_to_mm(10))
    # robot.turn(-140)
    #robot.straight(250)
    #robot.straight(-250)
    robot.settings(turn_rate=57)
    robot.turn(-45)
    robot.straight(library.inch_to_mm(26))
    robot.turn(-120)
    robot.straight(library.inch_to_mm(3)) #this forward hits the bench with the front of the attachment
    #robot.turn(-30)
    #robot.straight(library.inch_to_mm(12))
    robot.straight(library.inch_to_mm(-1.5))
    robot.drive(100, -40)
    wait(1250)
    robot.stop(Stop.BRAKE)
    robot.straight(library.inch_to_mm(1))
    robot.drive(110, 50)
    wait(1300)
    robot.stop(Stop.BRAKE)
    robot.straight(library.inch_to_mm(7))
    robot.stop()
    robot.turn(20)
    medium_motor.run_time(speed=500, time=2000)
    # medium_motor.run_time(speed=-10000, time=400)

    # Slide
    # Get over there from tire,
    # Knock down the first guy
    # Get the second guy to the top,
    # Second guy goes down,
    # Use the attachment to put the guys on a tire
    # Boccia
    # Get over there from slide,
    # Rotate boccia townards space where you can drop cubesw
    # Push the cube into the square, if we have time use bucket to add more
    # Bench
    
    
    # Tires
    # Drive over to the tires,
    # Go back to base
    # Flip the light tire east, 
    # Flip the heavy tire south,
    
    # Drive to Bocchia    
    # robot.turn(-27)
    # robot.straight(library.inch_to_mm(9.5))
    #library.line_follow_for_distance(distance=library.inch_to_mm(inch=15), p=1.9, sensor_lf=sensor_l)
    # robot.turn(50)
    # robot.straight(library.inch_to_mm(20))
    # #Boccia Code goes here.
    # robot.turn(10)
    # robot.stop()
    # robot.settings(straight_speed = 900)
    # robot.straight(library.inch_to_mm(-60))