from util import max_of_row_mins
if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    result = max_of_row_mins(matrix)
    print(result)
