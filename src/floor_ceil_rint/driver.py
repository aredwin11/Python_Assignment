from util import apply_numpy_operations
import numpy as np

if __name__ == '__main__':
    np.set_printoptions(legacy='1.13')
    numbers = list(map(float, input("Enter numbers separated by space: ").split()))
    floor, ceil, rint = apply_numpy_operations(numbers)

    print(floor)
    print(ceil)
    print(rint)
