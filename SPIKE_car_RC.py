from pybricks.pupdevices import Motor, Remote, UltrasonicSensor
from pybricks.parameters import Port, Direction, Stop, Button, Color
from pybricks.tools import wait, StopWatch

# Initialize the motors.
steer = Motor(Port.E, reset_angle=True)
drive = Motor(Port.C, Direction.COUNTERCLOCKWISE)
sonar = UltrasonicSensor(Port.D)

# Lower the acceleration so the car starts and stops realistically.
drive.control.limits(acceleration=1000)

# Connect to the remote.
remote = Remote()

steer.run_target(speed=300, target_angle=0)
sonar.lights.on((100,100,100,100))


sonarTimer = StopWatch()

def readSonar():
    distance = sonar.distance()
    if distance > 130:
        sonarTimer.reset()

    if sonarTimer.time() > 1000:
        sonar.lights.off()
        steer.run_target(speed=800, target_angle=-30)
        wait(300)
        steer.run_target(speed=800, target_angle=0)
        sonarTimer.reset()
        sonar.lights.on((100,100,100,100))
    return distance

proximityTimer = StopWatch()
# Now we can start driving!
while True:
    # Check which buttons are pressed.
    pressed = remote.buttons.pressed()

    # Choose the steer angle based on the right controls.
    steer_angle = 0
    if Button.RIGHT_MINUS in pressed:
        steer_angle -= 30
    if Button.RIGHT_PLUS in pressed:
        steer_angle += 30

    # Steer to the selected angle.
    steer.run_target(500, steer_angle, wait=False)

    # Choose the drive speed based on the left controls.
    drive_speed = 0
    if Button.LEFT_PLUS in pressed:
        drive_speed += 1000
    if Button.LEFT_MINUS in pressed:
        drive_speed -= 1000

    distance = readSonar()
    print(distance , "mm")

    # Apply the selected speed.
    if distance>300:
        proximityTimer.reset()
        #remote.light.on(Color.MAGENTA)
        #wait(10)
        #remote.light.on(Color.GREEN)

    if drive_speed > 0 and steer_angle==0 and proximityTimer.time() > 300:
        drive.brake()
        remote.light.on(Color.RED)
        #print(sonar.distance())
    else:
        drive.run(drive_speed)
        remote.light.on(Color.GREEN)        

    wait(10)

