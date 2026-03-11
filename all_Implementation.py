import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit

# Project Constants
X_MIN, X_MAX = -2.0, 1.0
Y_MIN, Y_MAX = -1.5, 1.5
MAX_ITER = 100

# 1. Naive Implementation (Nested Loops) 
def mandelbrot_naive(width, height):
    x_vals = np.linspace(X_MIN, X_MAX, width)
    y_vals = np.linspace(Y_MIN, Y_MAX, height)
    result = np.zeros((height, width))
    
    for i in range(height):
        for j in range(width):
            c = complex(x_vals[j], y_vals[i])
            z = 0j
            iteration = 0
            while abs(z) <= 2 and iteration < MAX_ITER:
                z = z**2 + c
                iteration += 1
            result[i, j] = iteration / MAX_ITER 
    return result
