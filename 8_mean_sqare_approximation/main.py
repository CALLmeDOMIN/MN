from numeric_methods import gauss_legendre_formula, lu_decomposition, horner_interpolation
from numpy import sin as np_sin, exp as np_exp, linspace as np_linspace, array as np_array, abs as np_abs
import matplotlib.pyplot as plt


def f_task(x):
    return np_exp(x) * np_sin(x/2) - x ** 3


def approx_integral(f, base, start, end):
    matrix = []
    intercept = []

    for i in range(len(base)):
        row = []
        for j in range(len(base)):
            row.append(gauss_legendre_formula(
                lambda x: x**(i + j), 4, start, end))
        matrix.append(row)
        intercept.append(gauss_legendre_formula(
            lambda x: ((x ** i) * f(x)), 4, start, end))

    return lu_decomposition(len(base), matrix, intercept)


start = -1
end = 1
base = [1, "x", "x^2", "x^3"]


x = np_linspace(start, end, 100)
coef = approx_integral(f_task, base, start, end)
real = np_array(f_task(x))
pred = [horner_interpolation(coef[::-1], x_i) for x_i in x]

plt.title("Integral Approximation w/ Gauss-Legendre, Base: [1, x, x^2, x^3]")
plt.plot(x, real, label="Real")
plt.plot(x, pred, label="Predicted")
plt.legend()
plt.show()

plt.title("Absolute Error")
plt.plot(x, np_abs(real - pred))
plt.show()
