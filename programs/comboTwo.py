# M03 - Slide

def comboTwo(robot, ev3, library, medium_motor, sensor_l, sensor_r):
    robot.stop()
    robot.settings(straight_speed=33)
    medium_motor.run_time(speed=200, time=2000, wait=False)
    robot.straight(library.inch_to_mm(3.5))
    robot.stop()
    robot.settings(straight_speed=100)
    robot.straight(library.inch_to_mm(-1.6))
    robot.straight(library.inch_to_mm(1.8))