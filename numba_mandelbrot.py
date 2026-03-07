import numpy as np
from numba import njit

@njit
def mandelbrot_numba(width, height, max_iter):

    xmin, xmax = -2, 1
    ymin, ymax = -1.5, 1.5

    result = np.zeros((height, width))

    for i in range(height):
        for j in range(width):

            x = xmin + (xmax - xmin) * j / width
            y = ymin + (ymax - ymin) * i / height

            c = complex(x, y)
            z = 0

            for n in range(max_iter):

                z = z*z + c

                if abs(z) > 2:
                    result[i, j] = n
                    break
            else:
                result[i, j] = max_iter

    return result