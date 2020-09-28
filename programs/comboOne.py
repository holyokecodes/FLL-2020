# M11 - Treadmill, M12 - Row Machine, M13 - Weight Machine

def comboOne(robot, ev3, library):
    #ev3.speaker.say("You pressed down, this button is not supported. DDDDDDDDDD")
    ## Use Library for line following to get to treadmill? Line follow to get back for sure
    
    robot.straight(library.inch_to_mm(15))
    library.line_follow_for_time()

    pass