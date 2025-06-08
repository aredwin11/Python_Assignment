def second_largest(arr):
    unique_nums = list(set(arr))
    if len(unique_nums) < 2:
        raise ValueError("Need at least two unique numbers.")
    unique_nums.sort()
    return unique_nums[-2]
