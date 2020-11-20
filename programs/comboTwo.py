#M08 - Boccia
#
def comboTwo(robot, ev3, library, medium_motor, sensor_l, sensor_r):
    # Drive to Bocchia    
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
    pass