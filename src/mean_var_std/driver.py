from util import calculate_value
if __name__ == '__main__':
    import numpy as np
    n, m = map(int, input("Enter rows and columns: ").split())
    matrix = [list(map(int, input(f"Enter row {i+1}: ").split())) for i in range(n)]
    mean_arr, var_arr, std_val = calculate_value(matrix)
    print(mean_arr)
    print(var_arr)
    print(std_val)
