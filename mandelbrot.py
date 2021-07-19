def mandelbrot(val1, val2):
    x, y = 0, 0
    for k in range(100):
        x, y = x**2 - y**2 + val1, 2 * x * y + val2
        if x**2 + y**2 >4:
            return k + 1
    return 0