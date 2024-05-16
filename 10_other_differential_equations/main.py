from matplotlib import pyplot as plt
from numpy import cbrt as np_cbrt, arange as np_arange, log as np_log
from numeric_methods import eulers_method


def huens_method(f, x, y, start, end, n):
    h = (end - start) / n
    result = []
    for _ in range(n):
        y += h / 2 * (f(y) + f(y + h * f(y)))
        x += h
        result.append((x, y))
    return result


def midpoint_method(f, x, y, start, end, n):
    h = (end - start) / n
    result = []
    for _ in range(n):
        y += h * f(y + h / 2 * f(y))
        x += h
        result.append((x, y))
    return result


def runge_kutta_method(f, x, y, start, end, n):
    h = (end - start) / n
    result = []
    for _ in range(n):
        k1 = h * f(y)
        k2 = h * f(y + k1 / 2)
        k3 = h * f(y + k2 / 2)
        k4 = h * f(y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        result.append((x, y))
    return result


def mse(real, calculated):
    return sum((r - c) ** 2 for r, c in zip(real, calculated)) / len(real)


def plot_results(correct, received, method_name):
    plt.plot([x[0] for x in correct], [x[1] for x in correct], label="correct")
    plt.plot([x[0] for x in received], [x[1]
             for x in received], label=method_name)
    plt.legend()
    plt.show()


ALFA = 10 ** -12
BETA = 0
x, T0 = 0, 1200
start, end, n = 0, 300, 100


def f(T):
    return -ALFA * (T ** 4 - BETA)


def correct_fun(x):
    return 30000 / (np_cbrt(15625 + 81 * x))


eulers = eulers_method(f, x, T0, start, end, n)
huens = huens_method(f, x, T0, start, end, n)
midpoint = midpoint_method(f, x, T0, start, end, n)
runge_kutta = runge_kutta_method(f, x, T0, start, end, n)
real = [(x, correct_fun(x)) for x, _ in eulers]

plot_results(real, eulers, "Euler's method")
plot_results(real, huens, "Huen's method")
plot_results(real, midpoint, "Midpoint method")
plot_results(real, runge_kutta, "Runge-Kutta method")

error_eulers = mse([x[1] for x in real], [x[1] for x in eulers])
error_huens = mse([x[1] for x in real], [x[1] for x in huens])
error_midpoint = mse([x[1] for x in real], [x[1] for x in midpoint])
error_runge_kutta = mse([x[1] for x in real], [x[1] for x in runge_kutta])

print(f"Euler's method error: {error_eulers}")
print(f"Huen's method error: {error_huens}")
print(f"Midpoint method error: {error_midpoint}")
print(f"Runge-Kutta method error: {error_runge_kutta}")


eulers_errors = []
huens_errors = []
midpoint_errors = []
runge_kutta_errors = []

for i in range(10, n):
    eulers = eulers_method(f, x, T0, start, end, i)
    huens = huens_method(f, x, T0, start, end, i)
    midpoint = midpoint_method(f, x, T0, start, end, i)
    runge_kutta = runge_kutta_method(f, x, T0, start, end, i)
    real = [(x, correct_fun(x)) for x, _ in eulers]

    eulers_errors.append(mse([x[1] for x in real], [x[1] for x in eulers]))
    huens_errors.append(mse([x[1] for x in real], [x[1] for x in huens]))
    midpoint_errors.append(mse([x[1] for x in real], [x[1] for x in midpoint]))
    runge_kutta_errors.append(
        mse([x[1] for x in real], [x[1] for x in runge_kutta]))

plt.plot(np_arange(10, n), np_log(eulers_errors), label="Euler's method")
plt.plot(np_arange(10, n), np_log(huens_errors), label="Huen's method")
plt.plot(np_arange(10, n), np_log(midpoint_errors), label="Midpoint method")
plt.plot(np_arange(10, n), np_log(
    runge_kutta_errors), label="Runge-Kutta method")
plt.title("Errors of methods in logarithmic scale")
plt.legend()
plt.show()
