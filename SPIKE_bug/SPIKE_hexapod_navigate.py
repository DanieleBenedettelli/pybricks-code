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

RADAR_ICON = Matrix(
    [
        [   0, 100, 100, 100,   0 ],
        [ 100,   0,   0,   0, 100 ],
        [   0,  50,  50,  50,   0 ],
        [   50,  0,   0,  0,   50 ],
        [   0,   0, 100,   0,   0 ],
    ]
)

def blink(up=True):
    eyes.lights.on((100)*4)
    if up:
        hub.speaker.play_notes(["F5/16", "G#5/16", "B5/8"], tempo=200)
    else:
        hub.speaker.play_notes(["B5/16", "G#5/16", "F5/8"], tempo=200)
    eyes.lights.on((0)*4)

bug.stop()
hub.display.icon(RADAR_ICON)
wait(1000)

while True:
    while eyes.distance() > 150:
        bug.forward()
    blink(False)
    while eyes.distance() < 160:
        bug.turnRight()
    bug.turnRight(1)
    blink(True)