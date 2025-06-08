import numpy as np

def apply_numpy_operations(numbers):
    arr = np.array(numbers)
    floor_result = np.floor(arr)
    ceil_result = np.ceil(arr)
    rint_result = np.rint(arr)
    return floor_result, ceil_result, rint_result
