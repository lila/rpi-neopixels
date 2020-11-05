#!/usr/bin/env python3

import colorsys
import time

import board
import neopixel


spacing = 360.0 / 16.0
hue = 0

pixels = neopixel.NeoPixel(board.D18, 5, brightness=.2, auto_write=False)

while True:
    hue = int(time.time() * 100) % 360
    for x in range(5):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        pixels[x] = (r, g, b)

    pixels.show()
    time.sleep(0.01)
