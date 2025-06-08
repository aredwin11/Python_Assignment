from util import second_largest

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter the numbers: ").split()))
    result = second_largest(arr)
    print(result)
