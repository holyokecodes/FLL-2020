from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# M09 - Tires, M03 - Slide, M08 - Boccia, M04 - Bench

def comboThree(robot, ev3, library):
    
    # Tires
    # Drive over to the tires,
    robot.straight(152.4)
    library.line_follow_for_distance_stop(distance=660, p=1)
    robot.turn(45)
    # Flip the light tire east, 
    # Flip the heavy tire south,
    # Slide
    # Get over there from tire,
    # Knock down the first guy
    # Get the second guy to the top,
    # Second guy goes down,
    # Use the attachment to put the guys on a tire
    # Boccia
    # Get over there from tire,
    # Rotate boccia townards space where you can drop cubesw
    # Push the cube into the square, if we have time use bucket to add more
    # Bench
    # Go to bench,
    # Run it over,
    # Go to position where bucket can obtain the top piece of the bench,
    # and take it.
    # Go back to base


    pass