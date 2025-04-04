import time
import numpy as np

def sum_numbers():
    start_time = time.time()
    total = 0
    for i in range(10_000_000):
        total += i
    end_time = time.time()
    print(f"Total sum (regular): {total}")
    print(f"Execution time (regular): {end_time - start_time:.6f} seconds")

def sum_numbers_numpy():
    start_time = time.time()
    total = np.sum(np.arange(10_000_000))
    end_time = time.time()
    print(f"Total sum (numpy): {total}")
    print(f"Execution time (numpy): {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    sum_numbers()
    print("\nNow using NumPy...")
    sum_numbers_numpy() 