import numpy as np

def mandelbrot_numpy(width, height, max_iter):

    xmin, xmax = -2, 1
    ymin, ymax = -1.5, 1.5

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)

    X, Y = np.meshgrid(x, y)

    C = X + 1j * Y
    Z = np.zeros_like(C)

    output = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):

        Z = Z**2 + C

        mask = np.abs(Z) > 2
        output[mask & (output == 0)] = i

        Z[mask] = 2

    return output