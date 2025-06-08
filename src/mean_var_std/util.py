import numpy as np

def calculate_value(matrix):
    arr = np.array(matrix)
    mean_result = np.mean(arr, axis=1)
    var_result = np.var(arr, axis=0)
    std_result = round(np.std(arr, axis=None), 11)
    return mean_result, var_result, std_result
