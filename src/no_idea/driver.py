from util import calculate_happiness

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    result = calculate_happiness(arr, A, B)
    print(result)
