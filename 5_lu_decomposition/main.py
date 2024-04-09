import numpy as np


def read_from_file(filename):
    a = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            a.append(line.split('\t'))
    a = [[float(i) for i in x] for x in a]
    return int(a[0][0]), a[2:], a[1]


np.set_printoptions(precision=2, suppress=True)


def print_matrix(matrix):
    np_matrix = np.array(matrix)
    print(np_matrix)
    print()


def print_lu(L, U):
    print('L:')
    print_matrix(L)
    print('U:')
    print_matrix(U)


def lu_decomposition(length, matrix, intercept):
    L = np.zeros((length, length))
    U = np.zeros((length, length))

    step = 0
    for i in range(length):
        L[i][i] = 1
        for j in range(i, length):
            sm = 0
            for k in range(i):
                sm += L[i][k] * U[k][j]
            U[i][j] = matrix[i][j] - sm
        print(f'step: {step}')
        print_lu(L, U)
        step += 1
        for j in range(i + 1, length):
            sm = 0
            for k in range(i):
                sm += L[j][k] * U[k][i]
            L[j][i] = (matrix[j][i] - sm) / U[i][i]
        print(f'step: {step}')
        print_lu(L, U)
        step += 1

    print("test:")
    print_matrix(np.dot(L, U) - matrix)

    z = np.zeros(length)
    for i in range(length):
        sm = 0
        for j in range(i):
            sm += L[i][j] * z[j]
        z[i] = intercept[i] - sm

    print('z:')
    print_matrix(z)

    print("test:")
    print_matrix(np.dot(L, z) - intercept)

    x = np.zeros(length)
    for i in range(length - 1, -1, -1):
        sm = 0
        for j in range(i + 1, length):
            sm += U[i][j] * x[j]
        x[i] = (z[i] - sm) / U[i][i]
    print('x:')
    print_matrix(x)

    return x


n, A, b = read_from_file('data.txt')

print(n)
print_matrix(A)
print_matrix(b)

x = lu_decomposition(n, A, b)

print("test:")
print(np.dot(A, x) - b)
