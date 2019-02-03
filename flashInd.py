# Write your code here :-)
from adafruit_circuitplayground.express import cpx
import time
while True:
    cpx.pixels[0] = (255, 0, 0)
    cpx.pixels[1] = (255, 255, 0)
    cpx.pixels[2] = (0, 255, 0)
    cpx.pixels[3] = (0, 255, 255)
    cpx.pixels[4] = (0, 0, 255)
    cpx.pixels[5] = (255, 255, 255)