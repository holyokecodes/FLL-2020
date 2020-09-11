#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class FuctionLibrary:
    def __init__(self, robot, ev3):
        #self, DriveBase, Hub
        self.driveBase = robot
        self.hub = ev3

    def lineFollowUntillBlack(self):
        pass

    def lineFollowForTime(self):
        pass
    
    def lineFollowForDistance(self):
        pass
