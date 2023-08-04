from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, Remote
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix
from Hexapod import Hexapod

# MAIN REMOTE-CONTROL
hub = PrimeHub()
bug = Hexapod(hub, Port.E, Port.A, Port.B)
eyes = UltrasonicSensor(Port.F)

def blink(up=True):
    eyes.lights.on((100)*4)
    if up:
        hub.speaker.play_notes(["F5/16", "G#5/16", "B5/8"], tempo=200)
    else:
        hub.speaker.play_notes(["B5/16", "G#5/16", "F5/8"], tempo=200)
    eyes.lights.on((0)*4)

# Connect to the remote.
hub.display.icon(Icon.FULL)
remote = Remote()
blink(True)

stopped = False

while True:
    pressed = remote.buttons.pressed()
    if len(pressed)>0:
        stopped = False

    if Button.RIGHT_MINUS in pressed:
        bug.turnLeft()
    elif Button.RIGHT_PLUS in pressed:
        bug.turnRight()
    elif Button.LEFT_PLUS in pressed:
        bug.forward()        
    elif Button.LEFT_MINUS in pressed:
        bug.backward()
    elif not stopped:
        bug.stop()
        stopped = True

#    if eyes.distance() < 160:
#        blink()
        