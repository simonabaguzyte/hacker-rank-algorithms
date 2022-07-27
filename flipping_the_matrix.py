def flippingMatrix(matrix):
    maximalSumOfSubmatrix = 0

    for i in range(n):
        for j in range(n):
            newMatrix = []
            newMatrix.append(matrix[i][j])
            newMatrix.append(matrix[(2 * n) - 1 - i][j])
            newMatrix.append(matrix[i][(2 * n) - 1 - j])
            newMatrix.append(matrix[(2 * n) - 1 - i][(2 * n) - 1 - j])

            maximalSumOfSubmatrix = maximalSumOfSubmatrix + max(newMatrix)

    return print(maximalSumOfSubmatrix)


if __name__ == '__main__':
    q = int(input("\nHow many matrices you want to create?: ").strip())

    for q_itr in range(q):
        n = int(input('How many rows do you want in your matrix (2n)?: ').strip())

        matrix = []
        for _ in range(2 * n):
            matrix.append(list(map(int, input("Fill the matrix (2n x 2n): ").rstrip().split())))

    result = flippingMatrix(matrix)

            