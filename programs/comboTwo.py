#M08 - Boccia, M05 - Basketball

def comboTwo(robot, ev3, library, medium_motor, sensor_b):
    """
    robot.turn(-27)
    
    robot.straight(library.inch_to_mm(9.5))
    library.line_follow_for_distance(distance=library.inch_to_mm(inch=15), p=1.9)
    robot.turn(35)
    """
    library.line_follow_for_distance(distance=library.inch_to_mm(inch=27), p=2.4)
    pass