import numpy as np
import matplotlib.pyplot as plt
import time
import all_Implementation



resolutions = [128, 256, 512, 1024]
benchmarks = []

for res in resolutions:
    # Time Naive
    s = time.time()
    all_Implementation.mandelbrot_naive(res, res)
    t_naive = time.time() - s
    
    # Time NumPy
    s = time.time()
    all_Implementation.mandelbrot_numpy(res, res)
    t_numpy = time.time() - s
    
    # Time Numba (Fastest)
    s = time.time()
    all_Implementation.mandelbrot_numba(res, res)
    t_numba = time.time() - s
    
    benchmarks.append([res, t_naive, t_numpy, t_numba])

import matplotlib.pyplot as plt

def visualize_mandelbrot(data):
    plt.figure(figsize=(10, 7))
    # 'magma' or 'inferno' are great for showing detail
    img = plt.imshow(data, extent=[X_MIN, X_MAX, Y_MIN, Y_MAX], cmap='magma')
    plt.colorbar(img, label='Iteration depth (normalized)')
    plt.title("Mandelbrot Set Visualization")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()

# Example usage with the Numba version
result = mandelbrot_numba(1024, 1024)
visualize_mandelbrot(result)

