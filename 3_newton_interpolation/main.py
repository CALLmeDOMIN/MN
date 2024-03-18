import time
from math import prod


def natural(a, x):
    iterations = len(a)
    return sum(a[k] * x ** k for k in range(iterations))


def horner(a, x):
    iterations = len(a)
    for k in range(iterations - 2, 0, -1):
        a[k] = a[k] + x * a[k + 1]
    return a[0] + x * a[1]


def newton(a, x):
    iterations = len(a)
    result = a[0]
    for k in range(1, iterations):
        result += diff_quot(a, k) * prod(x - a[i] for i in range(k))
    return result


def diff_quot(a, k):
    if k == 0:
        return a[0]
    else:
        return (diff_quot(a[1:], k - 1) - diff_quot(a[:-1], k - 1)) / (a[k] - a[0])


def read_data(filename):
    data, first, second = [], [], []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())

    for el in data[0].split('\t')[1:]:
        first.append(float(el[3:]))

    for el in data[1].split('\t')[1:]:
        second.append(float(el))

    return first, second


a_data, x_data = read_data("dataH.txt")

a_sampled = a_data[:4]
x_sampled = x_data[::5]

start = time.perf_counter_ns()
natural_value = [natural(a_sampled, x) for x in x_sampled]
end = time.perf_counter_ns()
natural_time = end - start

start = time.perf_counter_ns()
horner_value = [horner(a_sampled, x) for x in x_sampled]
end = time.perf_counter_ns()
horner_time = end - start

newton_value = [newton(a_sampled, x) for x in x_sampled]

print(f'natural_time={natural_time}, horner_time={horner_time}')

for i in range(len(x_sampled)):
    print(f'x={x_sampled[i]}, natural={natural_value[i]}, horner={
          horner_value[i]}, newton={newton_value[i]}')

x_data_n, y_data_n = read_data("dataN.txt")

x_sampled_n = x_data_n[::5]
y_sampled_n = y_data_n[::5]
