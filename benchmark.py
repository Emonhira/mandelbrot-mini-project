import time
from naive_mandelbrot import mandelbrot_naive
from numpy_mandelbrot import mandelbrot_numpy
from numba_mandelbrot import mandelbrot_numba

sizes = [200, 500, 1000]
max_iter = 100

for size in sizes:

    print(f"\nGrid Size: {size}x{size}")

    start = time.time()
    mandelbrot_naive(size, size, max_iter)
    t1 = time.time() - start

    start = time.time()
    mandelbrot_numpy(size, size, max_iter)
    t2 = time.time() - start

    start = time.time()
    mandelbrot_numba(size, size, max_iter)
    t3 = time.time() - start

    print("Naive:", t1)
    print("NumPy:", t2)
    print("Numba:", t3)

    print("Speedup NumPy:", t1/t2)
    print("Speedup Numba:", t1/t3)