def lagrange(x_points, y_points, x):
    n = len(x_points)
    result = 0
    for i in range(n):
        xi, yi = x_points[i], y_points[i]
        p = 1
        for j in range(n):
            xj = x_points[j]
            if i != j:
                p *= (x - xj) / (xi - xj)
        result += p * yi
    return result


def calculate_mse(y_points, interpolated_values):
    errors = [(y_points[i] - interpolated_values[i])
              ** 2 for i in range(len(y_points))]
    mse = sum(errors) / len(errors)
    return mse


def generate_linear_space(start, end, num):  # b)
    step = (end - start) / (num - 1)
    return [start + step * i for i in range(num)]


def f(x):  # b)
    return 1 / (1 + x ** 2)


def read_and_parse_data(filename):
    data = []

    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())

    x = []
    y = []

    for i in data[0].split('\t')[1:]:
        x.append(float(i))

    for i in data[1].split('\t')[1:]:
        y.append(float(i))

    return x, y


x_points, y_points = read_and_parse_data(filename="data.txt")

x_sampled = x_points[::5]
y_sampled = y_points[::5]

x_input = float(input('Podaj x: '))
y_interpolated = lagrange(x_sampled, y_sampled, x_input)
print(f"Wartość wielomianu interpolacyjnego w punkcie x = "
      f"{x_input} wynosi: {y_interpolated}")

interpolated_val = [lagrange(x_sampled, y_sampled, x) for x in x_points]
mse = calculate_mse(y_points, interpolated_val)
print(f"Błąd średniokwadratowy wynosi: {mse}")

for num_nodes in [5, 10, 15, 20, 25, 30]:  # b)
    x_nodes = generate_linear_space(-5, 5, num_nodes)
    y_nodes = [f(x) for x in x_nodes]

    x_range = generate_linear_space(-5, 5, 1000)
    y_true = [f(x) for x in x_range]
    y_interpolated = [lagrange(x_nodes, y_nodes, x) for x in x_range]
    mse = calculate_mse(y_true, y_interpolated)

    print(f"Wartość interpolacji dla {num_nodes} węzłów w punkcie x=0: "
          f"{lagrange(x_nodes, y_nodes, 0)}, a błąd średniokwadratowy wynosi: "
          f"{mse}")
