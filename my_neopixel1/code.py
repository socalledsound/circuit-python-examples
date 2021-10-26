import time
import board
# from rainbowio import colorwheel
import neopixel
import random


pixels = neopixel.NeoPixel(
    board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    for i in range(len(pixels)):
        pixels[i] = (r, g, b)
        pixels.show()
        time.sleep(0.1)
