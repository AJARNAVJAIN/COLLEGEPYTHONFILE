print("Name:ARNAV JAIN")
print("Roll no.:24BEE162")
class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Only 3x3 matrices are supported.")
        self.data = data

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __mul__(self, other):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)


# Example usage
if __name__ == "__main__":
    matrix1 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    matrix2 = Matrix([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    print("\nAddition:")
    print(matrix1 + matrix2)

    print("\nMultiplication:")
    print(matrix1 * matrix2)

    print("\nTranspose of Matrix 1:")
    print(matrix1.transpose())
