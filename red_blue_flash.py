# Flash Red and Blue
from adafruit_circuitplayground.express import cpx
import time

while True:
    cpx.pixels.fill((255, 0, 0))
    time.sleep(0.5)
    cpx.pixels.fill((0, 0, 255))
    time.sleep(0.5)