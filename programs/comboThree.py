from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# M09 - Tires, M03 - Slide, M08 - Boccia, M04 - Bench

def comboThree(robot, ev3, library, medium_motor):
    
    
    # Go to bench,
    # Run it over,
    # Go to position where bucket can obtain the top piece of the bench,
    # and take it.
    
    robot.turn(-65)
    robot.straight(462.6)
    robot.turn(-130)
    robot.straight(250)
    robot.straight(-250)
    
    """robot.turn(-100)
    robot.straight(400)
    robot.turn(90)
    """
    
    
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
    pass

    """# Drive to Bocchia    
    robot.turn(-27)
    robot.straight(library.inch_to_mm(9.5))
    library.line_follow_for_distance(distance=library.inch_to_mm(inch=15), p=1.9, sensor_lf=sensor_l)
    robot.turn(50)
    robot.straight(library.inch_to_mm(20))
    #Boccia Code goes here.
    robot.turn(10)
    robot.stop()
    robot.settings(straight_speed = 900)
    robot.straight(library.inch_to_mm(-60))
    pass"""