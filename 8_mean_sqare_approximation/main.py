from numeric_methods import gauss_legendre_formula, lu_decomposition, print_matrix, horner_interpolation, mse
from numpy import sin as np_sin, pi as np_pi, exp as np_exp, linspace as np_linspace, array as np_array
import matplotlib.pyplot as plt

base = [1, 1, 1, 1, 1]
start = 0
end = np_pi / 2


def f_sin(x):
    return np_sin(x)


def f_task(x):
    return np_exp(x) * np_sin(x/2) - x ** 3


def approx_integral(f, base, start, end):
    matrix = []
    intercept = []
    for i in range(len(base)):
        row = [gauss_legendre_formula(
            (lambda x: x**(i + j)), 4, start, end) for j in range(len(base))]
        intercept.append(gauss_legendre_formula(
            (lambda x: f(x) * (x ** i)), 4, start, end))
        matrix.append(row)
    return lu_decomposition(len(base), matrix, intercept)


approx_integral(f_sin, base, start, end)
coef = approx_integral(f_task, base, start, end)

x = np_linspace(-1, 1, 100)
pred = [horner_interpolation(coef, x_i) for x_i in x]
real = np_array(f_task(x))

plt.plot(x, pred, label='Predicted')
plt.plot(x, real, label='Real')
plt.legend()
plt.show()

print(mse(pred, real))
