from pybricks.pupdevices import Motor, Remote, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Direction, Stop, Button, Color, Axis
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
hub = PrimeHub(front_side=Axis.X, top_side = Axis.Z)

SPEED = 150
MAX_ERROR = 30

def wait_obstacle(distance, timeout):
    obstacleTimer = StopWatch()

    while obstacleTimer.time() < timeout:
        if sonar.distance() > distance :
            obstacleTimer.reset() 
        else :
            hub.speaker.beep(1000, 20)
            wait(50)

def read_distance(samples = 10):
    ave = 0
    for i in range(samples):
        ave += sonar.distance()
    return int(ave/samples)

def find_clearest_way():
    steer.run_target(500, 40)
    wait(500)
    distance_left = read_distance()
    
    steer.run_target(500, -40)
    wait(500)
    distance_right = read_distance()

    if distance_left > distance_right:
        steer.run_target(500, -30)
    else:
        steer.run_target(500, 30)


def wait_heading_change(angle_change=45, timeout=10000):
    timer = StopWatch()
    heading0 = hub.imu.heading()
    diff = 10
    while abs(diff) < angle_change and timer.time() < timeout :
        diff = hub.imu.heading() - heading0
        if diff > 180:
            diff -= 360
        if diff < -180:
            diff += 360
        #print(diff)
        wait(50)

while True:
    drive.run(300)
    wait_obstacle(distance=300, timeout=500)
    drive.stop()

    find_clearest_way()

    drive.run(-300)
    wait_heading_change(angle_change=35)
    drive.stop()

    steer.run_target(500, 0)        

    wait(1000)
