from matplotlib import pyplot as plt
from numpy import cbrt as np_cbrt


def eulers_method(f, x, y, start, end, n):
    h = (end - start) / n
    result = []
    for _ in range(n):
        y += h * f(y)
        x += h
        result.append((x, y))
    return result


ALFA = 10 ** -12
BETA = 0
x, T0 = 0, 1200
start, end, n = 0, 300, 10


def f(T):
    return -ALFA * (T ** 4 - BETA)


def correct_fun(x):
    return 30000 / (np_cbrt(15625 + 81 * x))


values = eulers_method(f, x, T0, start, end, n)
real = [(x, correct_fun(x)) for x, _ in values]

print(f'Last value of Euler\'s method: {values[-1][1]}')
print(f'Last value of real function: {real[-1][1]}')
print(f'Error: {abs(values[-1][1] - real[-1][1])}')

error = []

for i in range(1, n):
    euler = eulers_method(f, x, T0, start, end, i)
    real = [(x, correct_fun(x)) for x, _ in euler]
    error.append(abs(euler[-1][1] - real[-1][1]))

print("Error values")
for i in range(1, n):
    print(f'{i}: {error[i - 1]}')

plt.plot(*zip(*values), label='Euler\'s method')
plt.plot(*zip(*real), label='Real values')
plt.title("Euler's method vs Real values")
plt.legend()
plt.show()

plt.plot(range(1, n), error)
plt.title('Error')
plt.show()
