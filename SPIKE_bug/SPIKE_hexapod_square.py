from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix
from Hexapod import Hexapod

# MAIN NAVIGATION
hub = PrimeHub()
bug = Hexapod(hub, Port.E, Port.A, Port.B)
eyes = UltrasonicSensor(Port.F)

SQUARE_ICON = Matrix(
    [
        [ 100, 100, 100, 100, 100 ],
        [ 100,   0,   0,   0, 100 ],
        [ 100,   0,   0,   0, 100 ],
        [ 100,   0,    0,  0, 100 ],
        [ 100, 100, 100, 100, 100 ],
    ]
)

def blink(up=True):
    eyes.lights.on((100)*4)
    if up:
        hub.speaker.play_notes(["F5/16", "G#5/16", "B5/8"], tempo=200)
    else:
        hub.speaker.play_notes(["B5/16", "G#5/16", "F5/8"], tempo=200)
    eyes.lights.on((0)*4)

bug.stop(False)
hub.display.icon(SQUARE_ICON)
wait(1000)

for i in range(1):
    bug.forward(3)
    bug.turnRight(4)
bug.stop(True)
