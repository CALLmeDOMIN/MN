import time


def read_data(filename, offset=0, offset2=0):
    data, first, second = [], [], []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())

    for el in data[0].split('\t')[1:]:
        first.append(float(el[offset:]))

    for el in data[1].split('\t')[1:]:
        second.append(float(el[offset2:]))

    return first, second


def natural(a, x):
    if len(a) == 0:
        return 0
    return a[0] + sum(a[i] * x ** i for i in range(1, len(a)))


def horner(a, x):
    result = a[0]
    for i in range(1, len(a)):
        result = result * x + a[i]
    return result


def divided_diff(x, y):
    n = len(y)
    coef = y.copy()
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef


def newton(x, y, x_val):
    n = len(x)
    a = divided_diff(x, y)
    result = a[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_val - x[i]) + a[i]
    return result


def mse(y_true, y_pred):
    return sum((y_p - y_t) ** 2 for y_p, y_t in zip(y_pred, y_true)) / len(y_true)


def calculate_error(x_test, y_test, x_data, y_data):
    interpolated_values = [newton(x_data, y_data, x) for x in x_test]
    return mse(y_test, interpolated_values)


def most_accurate_result(x, y):
    n = len(x)
    best_count = 0
    best_accuracy = float('inf')

    for count in range(n + 1, 2, -1):
        step = max(1, n // count)
        x_sampled = x[::step]
        y_sampled = y[::step]

        error = calculate_error(x_sampled, y_sampled, x, y)

        if error < best_accuracy:
            best_accuracy = error
            best_count = count

    return best_count


a_data, x_data = read_data("dataH.txt", 3)  # 1

a_sampled = a_data[:4]
x_sampled = x_data[::5]

start = time.perf_counter_ns()
natural_value = [natural(a_sampled, x) for x in x_sampled]  # 2
end = time.perf_counter_ns()
natural_time = end - start

start = time.perf_counter_ns()
horner_value = [horner(a_sampled, x) for x in x_sampled]  # 3
end = time.perf_counter_ns()
horner_time = end - start

print(f'\nTiming:\nnatural_time='
      f'{natural_time}, horner_time={horner_time}')  # 4

print('\nResults:')
for i in range(len(x_sampled)):
    print(f'x={x_sampled[i]}, natural={natural_value[i]}, horner='
          f'{horner_value[i]}')

x_data_n, y_data_n = read_data("dataN.txt")  # 5

x_sampled_n = x_data_n[::5]
y_sampled_n = y_data_n[::5]

a_calculated = divided_diff(x_sampled_n, y_sampled_n)  # 5

print(f'\nCoefficienct calc:\na_calculated={a_calculated}')

best_node_count = most_accurate_result(x_data_n, y_data_n)  # 6
print(f'\nBest amount of nodes:\nbest_node_count={best_node_count}')

x_input = float(input("\nPodaj x dla newtona: "))  # 7
print(f'Wynik:\nnewton={newton(x_sampled_n, y_sampled_n, x_input)}')

y_interpolated = [horner(a_sampled, x) for x in x_sampled]

newton_dataH = [newton(x_sampled, y_interpolated, x) for x in x_sampled]

newton_dataN = [newton(x_sampled_n, y_sampled_n, x) for x in x_sampled_n]

mse_dataH = mse(newton_dataH, y_interpolated)
mse_dataN = mse(newton_dataN, y_sampled_n)

print(f'MSE for first dataset: {mse_dataH}')
print(f'MSE for second dataset: {mse_dataN}')
print(f'Difference: {abs(mse_dataH - mse_dataN)}')  # 8
