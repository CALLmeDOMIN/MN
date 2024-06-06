import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def f1(x):
    return np.log10(x**2 + 1) - x**3


def f2(x):
    return np.cosh(x) - np.sqrt(x)


def f3(x):
    if x == 0:
        return np.inf
    return np.exp(-x) + np.sin(x) - 1/x**2


def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print("Błąd: f(a) i f(b) muszą mieć różne znaki")
        return None

    iterations = []
    errors = []

    for _ in range(max_iter):
        c = (a + b) / 2
        iterations.append(c)
        errors.append(abs(func(c)))

        if abs(func(c)) < tol:
            return c, iterations, errors

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2, iterations, errors


def false_position_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print("Błąd: f(a) i f(b) muszą mieć różne znaki")
        return None

    iterations = []
    errors = []

    c = a
    for _ in range(max_iter):
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        iterations.append(c)
        errors.append(abs(func(c)))

        if abs(func(c)) < tol:
            return c, iterations, errors

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return c, iterations, errors


def find_opposite_sign_intervals(func, start, end, step=0.1):
    intervals = []
    x = start
    while x < end:
        if func(x) * func(x + step) < 0:
            intervals.append((x, x + step))
        x += step
    return intervals


def create_results_table(iterations, errors):
    return pd.DataFrame({
        'Iteracja': range(1, len(iterations) + 1),
        'Przybliżenie': iterations,
        'Błąd bezwzględny': errors
    })


def plot_iterations(method, iterations, errors, title):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    axs[0].plot(range(len(iterations)), iterations, 'o-')
    axs[0].set_title(f'{method} - Przybliżenia miejsc zerowych ({title})')
    axs[0].set_xlabel('Iteracja')
    axs[0].set_ylabel('Przybliżenie')

    axs[1].plot(range(len(errors)), errors, 'o-')
    axs[1].set_title(f'{method} - Błąd bezwzględny ({title})')
    axs[1].set_xlabel('Iteracja')
    axs[1].set_ylabel('Błąd')

    plt.tight_layout()
    plt.show()


functions = {
    'f1(x) = log10(x^2 + 1) - x^3': f1,
    'f2(x) = cosh(x) - sqrt(x)': f2,
    'f3(x) = exp(-x) + sin(x) - 1/x^2': f3
}

for name, func in functions.items():
    print(f"\nAnaliza funkcji: {name}")
    intervals = find_opposite_sign_intervals(func, 0.1, 7)

    if not intervals:
        print(f"Nie znaleziono odpowiednich przedziałów dla funkcji {
              name} w zakresie [0.1, 7].")
        continue

    all_roots_bisection = []
    all_roots_false_position = []

    for a, b in intervals:
        print(f"Analiza w przedziale: [{a:.3f}, {b:.3f}]")

        result_bisection = bisection_method(func, a, b)
        if result_bisection:
            root_bisection, iter_bisection, errors_bisection = result_bisection
            all_roots_bisection.append(root_bisection)
            print(f"Metoda bisekcji - pierwiastek: {root_bisection}")
            table_bisection = create_results_table(
                iter_bisection, errors_bisection)
            print(table_bisection)
            plot_iterations('Metoda bisekcji', iter_bisection,
                            errors_bisection, f"{name} [{a:.2f}, {b:.2f}]")

        result_false_position = false_position_method(func, a, b)
        if result_false_position:
            root_false_position, iter_false_position, errors_false_position = result_false_position
            all_roots_false_position.append(root_false_position)
            print(
                f"Metoda fałszywej linii - pierwiastek: {root_false_position}")
            table_false_position = create_results_table(
                iter_false_position, errors_false_position)
            print(table_false_position)
            plot_iterations('Metoda fałszywej linii', iter_false_position,
                            errors_false_position, f"{name} [{a:.2f}, {b:.2f}]")

    print(f"\nWszystkie pierwiastki znalezione metodą bisekcji dla {
          name}: {all_roots_bisection}")
    print(f"Wszystkie pierwiastki znalezione metodą fałszywej linii dla {
          name}: {all_roots_false_position}")
