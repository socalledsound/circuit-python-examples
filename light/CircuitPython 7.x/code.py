import time
import analogio
# import simpleio
import board
from rainbowio import colorwheel
import neopixel


num_pixels = 10

light = analogio.AnalogIn(board.LIGHT)

pixels = neopixel.NeoPixel(
    board.NEOPIXEL, num_pixels, brightness=1.0, auto_write=False)

BLUE = (0, 0, 255)


# def colorwheel(pos):
#     # Input a value 0 to 255 to get a color value.
#     # The colours are a transition r - g - b - back to r.
#     if pos < 0 or pos > 255:
#         return (0, 0, 0, 0)
#     if pos < 85:
#         return (255 - pos * 3, pos * 3, 0, 0)
#     if pos < 170:
#         pos -= 85
#         return (0, 255 - pos * 3, pos * 3, 0)
#     pos -= 170
#     return (pos * 3, 0, 255 - pos * 3, 0)


while True:
    # mapped_value = int(map_range((light.value), 0, 65520, 255, 0))

    # pixels.fill((mapped_value, 0, 0))
    # pixels.fill(((light.value/60000), 0, 0))
    # pixels.show()
    for i in range(len(pixels)):
        # pixels[i] = (colorwheel(i + (light.value) & 255))
        pixels[i] = (colorwheel((i * (light.value)) & 255))
        # pixels[i] = (255, 150, 0)
    pixels.show()
    time.sleep(0.1)
