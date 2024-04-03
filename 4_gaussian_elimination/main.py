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


def gaussian_elimination(matrix, intercept):
    step = 1
    for k in range(len(matrix)):
        for i in range(k + 1, len(matrix)):
            print(f'Step {step}:')
            if matrix[k][k] == 0:
                matrix_pivoting(matrix)
            try:
                factor = matrix[i][k] / matrix[k][k]
            except ZeroDivisionError:
                factor = 0
            for j in range(k, len(matrix)):
                matrix[i][j] -= factor * matrix[k][j]
                intercept[i] -= factor * intercept[k]
                if matrix[i][j] < 10 ** -10 and matrix[i][j] > -10 ** -10:
                    matrix[i][j] = 0.0
            matrix[i][len(matrix) - 1] -= factor * matrix[k][len(matrix) - 1]
            print_matrix(matrix)
            print(intercept)
            print()
            step += 1


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


def matrix_pivoting(matrix):
    for i in range(len(matrix)):
        max_value = matrix[i][i]
        max_index = i
        for j in range(i + 1, len(matrix)):
            if abs(matrix[j][i]) > abs(max_value):
                max_value = matrix[j][i]
                max_index = j
        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]

    return matrix


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

if is_linear_independent_a == False:
    gaussian_elimination(matrix_a, intercept_a)
    print_matrix(matrix_a)

if is_linear_independent_b == False:
    gaussian_elimination(matrix_b, intercept_b)
    print_matrix(matrix_b)

if is_linear_independent_c == False:
    gaussian_elimination(matrix_c, intercept_c)
    print_matrix(matrix_c)

print(intercept_a)
print(intercept_b)
print(intercept_c)
