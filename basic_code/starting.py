from pyfirmata import ArduinoNano
from time import sleep
board = ArduinoNano('/dev/ttyUSB0')

# enable pins
board.digital[5].write(1)
board.digital[10].write(1)

rmp = board.get_pin("d:6:p")  # right plus pin
rpp = board.get_pin("d:7:o")  # right minus pin
lmp = board.get_pin("d:9:p")  # left plus pin
lpp = board.get_pin("d:8:o")  # left minus pin

def go(speed = 0):
    if speed == 0:
        lmp.write(0)
        lpp.write(0)
        rmp.write(0)
        rpp.write(0)
    elif speed > 0:
        lmp.write(0)
        lpp.write(speed)
        rmp.write(0)
        rpp.write(speed)
    elif speed < 0:
        lmp.write(1)
        lpp.write(1 + speed)
        rmp.write(1)
        rpp.write(1 + speed)

def spin(speed = 0):
    if speed == 0:
        lmp.write(0)
        lpp.write(0)
        rmp.write(0)
        rpp.write(0)
    elif speed > 0:
        lmp.write(0)
        lpp.write(speed)
        rmp.write(1)
        rpp.write(1 - speed)
    elif speed < 0:
        lmp.write(1)
        lpp.write(1 + speed)
        rmp.write(0)
        rpp.write(-speed)

if __name__ == "__main__":
    speed = 1
    go(speed)
    sleep(3)
    go(-speed)
    sleep(3)
    spin(speed)
    sleep(2)
    spin(-speed)
    sleep(2.05)
    go()