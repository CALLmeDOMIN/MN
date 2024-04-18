import numpy as np

p_2 = [-1 / np.sqrt(3), 1 / np.sqrt(3)]
w_2 = [1, 1]

p_3 = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
w_3 = [5/9, 8/9, 5/9]

p_4 = [-np.sqrt((3 + 2*np.sqrt(6/5))/7), -np.sqrt((3 - 2*np.sqrt(6/5))/7),
       np.sqrt((3 - 2*np.sqrt(6/5))/7), np.sqrt((3 + 2*np.sqrt(6/5))/7)]
w_4 = [(18 - np.sqrt(30))/36, (18 + np.sqrt(30))/36,
       (18 + np.sqrt(30))/36, (18 - np.sqrt(30))/36]

p_5 = [-1/3 * np.sqrt(5 + 2*np.sqrt(10/7)), -1/3 * np.sqrt(5 - 2*np.sqrt(10/7)),
       0, 1/3 * np.sqrt(5 - 2*np.sqrt(10/7)), 1/3 * np.sqrt(5 + 2*np.sqrt(10/7))]
w_5 = [(322 - 13*np.sqrt(70))/900, (322 + 13*np.sqrt(70))/900, 128 /
       225, (322 + 13*np.sqrt(70))/900, (322 - 13*np.sqrt(70))/900]


def f1(x):
    return 5*x**3 - 12*x**2 - x + 3


def f2(x):
    return x**2 * np.sin(x)**3


def f3(x):
    return np.exp(x ** 2) * (1 - x)


start_1, end_1, expected_1 = -2, 3, -46.250005
start_2, end_2, expected_2 = 1, 4.8, -10.9001
start_3, end_3, expected_3 = -1.5, 3.2, -9358.63


def g_l_quadrature(f, n, start, end):
    p, w = [], []

    if n == 2:
        p, w = p_2, w_2
    elif n == 3:
        p, w = p_3, w_3
    elif n == 4:
        p, w = p_4, w_4
    elif n == 5:
        p, w = p_5, w_5

    integral = 0
    for i in range(n):
        integral += w[i] * f((end - start) / 2 * p[i] + (start + end) / 2)

    return (end - start) / 2 * integral


def generate_ranges(amount, start, end):
    ranges = []
    step = (end - start) / amount
    for i in range(amount):
        ranges.append((start + i * step, start + (i + 1) * step))
    return ranges


def result_with_division(f, n, start, end, amount):
    ranges = generate_ranges(amount, start, end)
    result = 0
    for r in ranges:
        result += g_l_quadrature(f, n, r[0], r[1])
    return result


print("1. Example")
print("f(x) = 5*x^3 - 12*x^2 - x + 3")
value = g_l_quadrature(f1, 2, start_1, end_1)
print(f'2 points: {value}, expected: '
      f'{expected_1}, error: {abs(value - expected_1)}')

print("\n2. Task 1")
print("f(x) = x^2 * sin(x)^3")
for i in range(2, 5):
    value = g_l_quadrature(f2, i, start_2, end_2)
    value_with_division = result_with_division(f2, i, start_2, end_2, 10)
    print(f'{i} points: {value}, expected: '
          f'{expected_2}, error: {abs(value - expected_2)}')
    print(f'{i} points with division: {value_with_division}, expected: '
          f'{expected_2}, error: {abs(value_with_division - expected_2)}')

print("\n3. Task 2")
print("f(x) = exp(x^2) * (1 - x)")
for i in range(2, 5):
    value = g_l_quadrature(f3, i, start_3, end_3)
    value_with_division = result_with_division(f3, i, start_3, end_3, 10)
    print(f'{i} points: {value}, expected: '
          f'{expected_3}, error: {abs(value - expected_3)}')
    print(f'{i} points with division: {value_with_division}, expected: '
          f'{expected_3}, error: {abs(value_with_division - expected_3)}')
