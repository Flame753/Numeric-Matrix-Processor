def create_matrices():
    row_size, col_size = [int(num) for num in str(input()).split()]
    # x: columns and y: rows
    return list([int(x) for x in str(input()).split()] for y in range(row_size))


def check_matrices(matrix_A, matrix_B) -> bool:
    row_A = len(matrix_A)
    row_B = len(matrix_B)
    col_A = [len(row) for row in matrix_A]
    col_B = [len(row) for row in matrix_B]

    if row_A == row_B and col_A == col_B:
        return True
    print('ERROR')


def display_matrix(matrix):
    for row in matrix:
        print(str(row).strip('[]').replace(',', ''))


def add_matrices(matrix_A, matrix_B):
    matrix = []
    new_row = []
    if check_matrices(matrix_A, matrix_B):
        for row in range(len(matrix_A)):
            for col in range(len(matrix_A[0])):
                num = matrix_A[row][col] + matrix_B[row][col]
                new_row.append(num)
            matrix.append(new_row.copy())
            new_row.clear()
        display_matrix(matrix)


def scalar_multiply(matrix_A, scalar):
    matrix = []
    new_row = []
    for row in range(len(matrix_A)):
        for col in range(len(matrix_A[0])):
            num = matrix_A[row][col] * scalar
            new_row.append(num)
        matrix.append(new_row.copy())
        new_row.clear()
    display_matrix(matrix)


if __name__ == "__main__":
    a = create_matrices()
    #b = create_matrices()
    # add_matrices(a, b)
    scalar_multiply(a, int(input()))
