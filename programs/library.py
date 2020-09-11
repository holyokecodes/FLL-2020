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

    def shutDown(self):
        self.hub.speaker.say("Logic error, error error error error error error error error error error errorrr Non halting program detected, shutting down")
        self.hub.speaker.play_notes(['C4/4', 'F3/4', 'F2/4'])

    def lineFollowUntillBlack(self):
        pass

    def lineFollowForTime(self):
        pass

    def lineFollowForDistance(self):
        pass
