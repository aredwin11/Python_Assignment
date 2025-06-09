import numpy as np
def max_of_row_mins(matrix):
    """
    Given a 2D list (matrix), returns the maximum of the minimum values of each row.
    """
    arr = np.array(matrix)
    row_mins = np.min(arr, axis=1)
    return np.max(row_mins)
