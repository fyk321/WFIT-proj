# FRAKTAL MANDELBROTA
import random

import numpy
from PIL import Image
from mandelbrot import mandelbrot

def color(val):
    r = colors[val//modr % 4]
    g = colors[(val//modg) % 4]
    b = colors[(val//modb) % 4]
    return (r, g, b)

if __name__ == "__main__":
    zoom = 1 #skala powiększenia

    pixels = 200 * zoom
    x = 3 / zoom
    y = 3 / zoom
    xs = -2
    ys = -1.5/zoom

    colors = [0,0,0,0]
    colors[0] = random.randint(0,255) #kolor pixeli nalezacych do zbioru madnelbrota, 255- biale, 0 - czarne
    colors[1] = random.randint(0,255)
    colors[2] = random.randint(0,255)
    colors[3] = random.randint(0,255)
    modr = random.randint(1,2)
    modg = random.randint(3, 8)
    modb = random.randint(9, 16)
    im_width = int(pixels * x)
    im_height = int(pixels * y)

    array = numpy.zeros((im_height,
                         im_width,
                         3),
                        dtype = numpy.uint8)

    for i in range(im_width):
        val1 = xs + i / pixels
        for j in range(im_height):
            val2 = ys + j / pixels
            val = mandelbrot(val1, val2)
            array[j, i,] = color(val)

    img = Image.fromarray(array)
    img.save('fractal.png')
    img.show()