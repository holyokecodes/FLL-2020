# M11 - Treadmill, M12 - Row Machine, M13 - Weight Machine

def comboOne(robot, ev3, library):
    #ev3.speaker.say("You pressed down, this button is not supported. DDDDDDDDDD")
    ## Use Library for line following to get to treadmill? Line follow to get back for sure
    robot.straight(library.inch_to_mm(8.5))
    robot.turn(-20)
    library.line_follow_for_distance(p=-1, distance=library.inch_to_mm(58.4645))
    # ev3.speaker.say("That was " + str(library.mm_to_inch(robot.distance())) + " Inches")
    robot.straight(library.inch_to_mm(8.75))
    pass