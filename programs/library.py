#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from math import *

class FuctionLibrary:
    def __init__(self, robot, ev3, left_motor, right_motor):
        #self, DriveBase, Hub
        self.driveBase = robot
        self.hub = ev3

        self.left_motor = left_motor
        self.right_motor = right_motor

        self.left_motor.reset_angle(0)
        self.left_motor.reset_angle(0)

    def shutDown(self):
        self.hub.speaker.say("Shutting down...")
        self.hub.speaker.play_notes(['C4/4', 'F3/4', 'F2/4'])

    def lineFollowUntilBlack(self, PROPORTIONAL_GAIN=1.2, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_b=0, debug=False):
        BLACK = 9 #what is black
        WHITE = 85 #what is white, also what is life (42)
        threshold = (BLACK + WHITE) / 2 #the center of black+white

        while True: #forever, do

            if (debug):
                print(sensor_b.reflection()) #how bright the stuff the color sensor sees is
            #Calculate the turn rate from the devation and set the drive base speed and turn rate.
            self.driveBase.drive(DRIVE_SPEED, PROPORTIONAL_GAIN * sensor_b.reflection() - threshold)
            
            #stop condition 
            #if sensor_a.reflection() > 80: #
            #    self.shutDown()
            #    return #STOP THEIF
    

    def lineFollowForTime(self):
        pass

    def lineFollowForDistance(self, PROPORTIONAL_GAIN=1, DRIVE_SPEED=100, BLACK=9, WHITE= 85, sensor_b=0, distance=1000, debug=False):
        BLACK = 9 #what is black
        WHITE = 85 #what is white, also what is life (42)
        threshold = (BLACK + WHITE) / 2 #the center of black+white

        while True: #forever, do

            if (debug):
                print(sensor_b.reflection()) #how bright the stuff the color sensor sees is
            #Calculate the turn rate from the devation and set the drive base speed and turn rate.
            self.driveBase.drive(DRIVE_SPEED, PROPORTIONAL_GAIN * sensor_b.reflection() - threshold)
            
            #stop condition 
            if self.driveBase.distance() > distance: #
                break #STOP THEIF
        self.hub.speaker.say("I have reached " + str(math.floor(distance/25.4, 2)) + "inches")
        