from util import calculate_determinant

if __name__ == '__main__':
    n = int(input("Enter size of square matrix (n): "))
    matrix = []

    for _ in range(n):
        row = list(map(float, input("Enter row values: ").split()))
        matrix.append(row)

    result = calculate_determinant(matrix)
    print(result)
