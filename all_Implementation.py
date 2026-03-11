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

# 2. NumPy Implementation (Vectorized) 
def mandelbrot_numpy(width, height):
    x = np.linspace(X_MIN, X_MAX, width)
    y = np.linspace(Y_MIN, Y_MAX, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros(C.shape, dtype=complex)
    M = np.full(C.shape, MAX_ITER, dtype=float)
    
    for i in range(MAX_ITER):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + C[mask]
        escaped = (np.abs(Z) > 2) & (M == MAX_ITER)
        M[escaped] = i
        
    return M / MAX_ITER

# 3. Numba Implementation (JIT Compiled)
@jit(nopython=True)
def mandelbrot_numba_core(width, height, x_vals, y_vals):
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

def mandelbrot_numba(width, height):
    x_vals = np.linspace(X_MIN, X_MAX, width)
    y_vals = np.linspace(Y_MIN, Y_MAX, height)
    return mandelbrot_numba_core(width, height, x_vals, y_vals)