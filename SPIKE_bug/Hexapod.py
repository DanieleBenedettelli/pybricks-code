from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix

SHIFT_ANGLE = 150
STEP_ANGLE = 20
TURN_ANGLE = 18
PAUSE = 280 # ms
SPEED = 1000

class Hexapod :

    def __init__(self, hub, shifterMotorPort = Port.E, leftMotorPort = Port.A, rightMotorPort = Port.B):
        self.__hub = hub
        self.shiftingLegs = Motor(shifterMotorPort, reset_angle=True)
        self.rightLegs = Motor(rightMotorPort, reset_angle=True)
        self.leftLegs = Motor(leftMotorPort, reset_angle=True)
        self.__motors = (self.shiftingLegs, self.rightLegs, self.leftLegs)
        self.__steppingMotors = (self.rightLegs, self.leftLegs)
        [m.control.limits(speed = 1500, acceleration=6000) for m in self.__motors]

    def __shift(self, side=1):
        self.shiftingLegs.run_target(speed = SPEED, target_angle = side*SHIFT_ANGLE, wait=False)

    def __step(self, L=1, R=1):
        self.leftLegs.run_target(speed = SPEED, target_angle=L*STEP_ANGLE, wait=False)
        self.rightLegs.run_target(speed = SPEED, target_angle=R*STEP_ANGLE, wait=False)


    def stop(self, waitForCompletion=False):
        self.__hub.display.icon(Icon.PAUSE)
        self.__step(0,0)
        #self.rightLegs.run_target(speed = SPEED, target_angle=0, wait=False)
        #self.leftLegs.run_target(speed = SPEED, target_angle=0, wait=False)
        wait(500)
        self.__shift(0)
        while waitForCompletion and not self.shiftingLegs.done():
            wait(100)
        #self.shiftingLegs.run_target(speed = SPEED, target_angle=0, wait=False)

    def forward(self, steps = 1):
        self.__hub.display.icon(Icon.ARROW_UP)
        for i in range(steps):
            self.__shift(1)
            wait(PAUSE)
            self.__step(1,1)
            wait(PAUSE)
            self.__shift(-1)
            wait(PAUSE)
            self.__step(-1,-1)
            wait(PAUSE)

    def backward(self, steps = 1):
        self.__hub.display.icon(Icon.ARROW_DOWN)
        for i in range(steps):
            self.__shift(1)
            wait(PAUSE)
            self.__step(-1,-1)
            wait(PAUSE)
            self.__shift(-1)
            wait(PAUSE)
            self.__step(1,1)
            wait(PAUSE)               

    def turnRight(self, steps = 1):
        self.__hub.display.icon(Icon.CLOCKWISE)
        for i in range(steps):
            self.__shift(1)
            wait(PAUSE)
            self.__step(1,-1)
            wait(PAUSE)
            self.__shift(-1)
            wait(PAUSE)
            self.__step(-1,1)
            wait(PAUSE)

    def turnLeft(self, steps = 1):
        self.__hub.display.icon(Icon.COUNTERCLOCKWISE)
        for i in range(steps):
            self.__shift(1)
            wait(PAUSE)
            self.__step(-1,1)
            wait(PAUSE)
            self.__shift(-1)
            wait(PAUSE)
            self.__step(1,-1)
            wait(PAUSE)        
