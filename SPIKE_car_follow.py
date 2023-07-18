from pybricks.pupdevices import Motor, Remote, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Direction, Stop, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub

# Initialize the motors.
steer = Motor(Port.E, reset_angle=True)
drive = Motor(Port.C, Direction.COUNTERCLOCKWISE)
sonar = UltrasonicSensor(Port.D)
color = ColorSensor(Port.F)


# Lower the acceleration so the car starts and stops realistically.
drive.control.limits(acceleration=1000)
steer.control.limits(acceleration=1000)

steer.run_target(speed=300, target_angle=0)
#sonar.lights.on((100,100,100,100))

timer = StopWatch()
hub = PrimeHub()

SPEED = 150
MAX_ERROR = 30

while timer.time() < 1500:
    reading = color.reflection()
    error = 50 - reading
    steer_angle = 0.5*error
    err_rel = abs(error)/MAX_ERROR
    drive_speed = (1.1 - err_rel)*SPEED
    print(reading, steer_angle, drive_speed)
    steer.run_target(600, steer_angle, wait=False)
    drive.run(SPEED)

    if reading < 90:
        timer.reset()

drive.stop()        
hub.speaker.play_notes(["A4/8", "R/8", "A4/4"])


