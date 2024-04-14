from numeric_methods import horner_interpolation
from math import cos


def read_from_file(filename):
    degree, coeff, start, end = 0, [], 0, 0
    with open(filename, 'r') as file:
        degree = int(file.readline())
        coeff = list(map(int, file.readline().split()))
        start, end = map(int, file.readline().split())

    return degree, coeff[::-1], start, end


def f(x):
    return x * cos(x)**3


def trapezoidal_formula(f, n, a, b):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        result += f(a + i * h)

    result *= h

    return result


def simpson_formula(f, n, a, b):
    n *= 2
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]

    integral = f(x[0]) + f(x[-1])

    for i in range(1, n, 2):
        integral += 4 * f(x[i])

    for i in range(2, n-1, 2):
        integral += 2 * f(x[i])

    integral *= h / 3

    return integral


degree, a_i, a, b = read_from_file('data.txt')

n = 100
print(f"Values for n = {n}")
print(trapezoidal_formula(lambda x: horner_interpolation(a_i, x), n, a, b))
print(simpson_formula(lambda x: horner_interpolation(a_i, x), n, a, b))

n = 100
print(f"\nValues for n = {n}")
first_trap = trapezoidal_formula(
    lambda x: horner_interpolation(a_i, x), n, a, b)
first_simp = simpson_formula(lambda x: horner_interpolation(a_i, x), n, a, b)
print(f"Trap: {first_trap}\nSimp: {first_simp}")

first_Expected = 707.7

print("\nExpected vs calculated value")
print(f"Trap: {first_Expected} vs {first_trap} diff: "
      f"{first_Expected - first_trap}")
print(f"Simp: {first_Expected} vs {first_simp} diff: "
      f"{first_Expected - first_simp}")

a, b = 3.5, 6.5296718531238060
print(f"\nValues for a = {a} and b = {b} and n = {n}")
integral_trap = trapezoidal_formula(f, n, a, b)
integral_simp = simpson_formula(f, n, a, b)
print(f"Trap: {integral_trap}\nSimp: {integral_simp}")

second_Expected = 4.2024

print("\nExpected vs calculated value")
print(f"Trap: {second_Expected} vs {integral_trap} diff: "
      f"{second_Expected - integral_trap}")
print(f"Simp: {second_Expected} vs {integral_simp} diff: "
      f"{second_Expected - integral_simp}")
