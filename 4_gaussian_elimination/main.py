import numpy as np


def read_data(filename):
    data, intercept, matrix = [], [], []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    n = int(data[0])

    for el in data[1].split('\t'):
        intercept.append(int(el))

    for i in range(2, len(data)):
        row = []
        for el in data[i].split('\t'):
            row.append(int(el))
        matrix.append(row)

    return n, intercept, matrix


np.set_printoptions(precision=2)


def print_matrix(matrix):
    np_matrix = np.array(matrix)
    print(np_matrix)
    print()


def matrix_pivoting(matrix, intercept, k):
    max_value = matrix[k][k]
    max_index = k
    for j in range(k + 1, len(matrix)):
        if abs(matrix[j][k]) > abs(max_value):
            max_value = matrix[j][k]
            max_index = j
    matrix[k], matrix[max_index] = matrix[max_index], matrix[k]
    intercept[k], intercept[max_index] = intercept[max_index], intercept[k]


def gaussian_elimination(matrix, intercept):
    for k in range(len(matrix)):
        matrix_pivoting(matrix, intercept, k)
        if matrix[k][k] == 0:
            continue
        for i in range(k + 1, len(matrix)):
            factor = matrix[i][k] / matrix[k][k]
            for j in range(k, len(matrix)):
                matrix[i][j] -= factor * matrix[k][j]
            intercept[i] -= factor * intercept[k]
        print("Step", k+1)
        print("Matrix:")
        print_matrix(matrix)
        print("Intercept:")
        print_matrix(intercept)
        print("\n")


def back_substitution(matrix, intercept):
    n = len(matrix)
    for i in range(n - 1, -1, -1):
        intercept[i] = (intercept[i] - sum(matrix[i][j] * intercept[j]
                        for j in range(i + 1, n))) / matrix[i][i]
    return intercept


def is_linear_independent(matrix):
    is_linear_independent_global = False

    for i in range(1, len(matrix) - 1):
        if matrix[i][0] == 0 or matrix[i - 1][0] == 0:
            factor = 0
        else:
            factor = matrix[i][0] / matrix[i - 1][0]
        is_linear_independent = True
        for j in range(1, len(matrix)):
            if matrix[i][j] == 0 or matrix[i - 1][j] == 0:
                factor2 = 0
            else:
                factor2 = matrix[i][j] / matrix[i - 1][j]
            if factor != factor2:
                is_linear_independent = False
                break
        if is_linear_independent:
            is_linear_independent_global = True
            break

    return is_linear_independent_global


n_a, intercept_a, matrix_a = read_data('dataA.txt')
n_b, intercept_b, matrix_b = read_data('dataB.txt')
n_c, intercept_c, matrix_c = read_data('dataC.txt')

print_matrix(matrix_a)
print_matrix(matrix_b)
print_matrix(matrix_c)

is_linear_independent_a = is_linear_independent(matrix_a)
is_linear_independent_b = is_linear_independent(matrix_b)
is_linear_independent_c = is_linear_independent(matrix_c)

print(is_linear_independent_a)
print(is_linear_independent_b)
print(is_linear_independent_c)
print()

if not is_linear_independent_a:
    gaussian_elimination(matrix_a, intercept_a)
    back_substitution(matrix_a, intercept_a)

if not is_linear_independent_b:
    gaussian_elimination(matrix_b, intercept_b)
    back_substitution(matrix_b, intercept_b)

if not is_linear_independent_c:
    gaussian_elimination(matrix_c, intercept_c)
    back_substitution(matrix_c, intercept_c)

print(intercept_a)
print(intercept_b)
print(intercept_c)
