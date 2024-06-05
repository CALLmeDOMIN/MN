from numpy import sin as np_sin, cos as np_cos, linspace as np_linspace, sqrt as np_sqrt


def newtons_method(f, df, x0, tol=1e-6, max_iter=1000, eps=1e-6):
    x = x0
    for i in range(max_iter):
        try:
            x_new = x - f(x)/(df(x) + eps)
        except ZeroDivisionError:
            return None, i+1
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x_new, i+1


def secant_method(f, x0, x1, tol=1e-6, max_iter=1000, eps=1e-6):
    x = x0
    x_prev = x1
    for i in range(max_iter):
        try:
            x_new = x - f(x)*(x - x_prev)/(f(x) - f(x_prev) + eps)
        except ZeroDivisionError:
            return None, i+1
        if abs(x_new - x) < tol:
            break
        x_prev = x
        x = x_new
    return x_new, i+1


def find_roots(f, df, interval, num_guesses, tol=1e-6, max_iter=1000, method='newtons'):
    roots = []
    initial_guesses = np_linspace(interval[0], interval[1], num_guesses)
    for x0 in initial_guesses:
        if method == 'newtons':
            x, _ = newtons_method(f, df, x0, tol, max_iter)
        elif method == 'secant':
            x, _ = secant_method(f, x0, x0 + 1, tol, max_iter)
        roots.append(x)
    return roots


def print_roots(roots, real_roots):
    for i, root in enumerate(roots):
        try:
            closest_real_root = min(
                real_roots, key=lambda real_root: abs(real_root - root))
            error = abs(root - closest_real_root)
            print(f'Root {i+1}: {root:.6f} '
                  f'Closest Real Root: {closest_real_root:.6f} error: {error}')
        except TypeError:
            print(f'Root {i+1}: None')


def fun(x):
    return x**2 - 2


def fun2(x):
    return x**3 + x**2 - 3*x - 3


def fun3(x):
    return np_sin(x**2) - x**2


def fun4(x):
    return np_sin(x**2) - x**2 + 1/2


def dfun(x):
    return 2*x


def dfun2(x):
    return 3*x**2 + 2*x - 3


def dfun3(x):
    return 2*x*(np_cos(x**2) - 1)


print('Problem 1:\nNewton\'s Method:')
interval = (-2, 2)
num_guesses = 10
roots = find_roots(fun, dfun, interval, num_guesses)
real_roots = [-np_sqrt(2), np_sqrt(2)]
print_roots(roots, real_roots)

print('\nSecant Method:')
roots = find_roots(fun, dfun, interval, num_guesses, method='secant')
print_roots(roots, real_roots)

print('\nProblem 2:\nNewton\'s Method:')
interval = (-2, 2)
num_guesses = 10
roots = find_roots(fun2, dfun2, interval, num_guesses)
real_roots = [-np_sqrt(3), -1, np_sqrt(3)]
print_roots(roots, real_roots)

print('\nSecant Method:')
num_guesses = 10
roots = find_roots(fun2, dfun2, interval, num_guesses, method='secant')
print_roots(roots, real_roots)

print('\nProblem 3:\nNewton\'s Method:')
interval = (-2, 2)
num_guesses = 20
roots = find_roots(fun3, dfun3, interval, num_guesses)
real_roots = [0]
print_roots(roots, real_roots)

print('\nSecant Method:')
roots = find_roots(fun3, dfun3, interval, num_guesses, method='secant')
print_roots(roots, real_roots)

print('\nProblem 4:\nNewton\'s Method:')
interval = (-2, 2)
num_guesses = 10
roots = find_roots(fun4, dfun3, interval, num_guesses)
real_roots = [-1.22364226352962, 1.22364226352962]
print_roots(roots, real_roots)

print('\nSecant Method:')
roots = find_roots(fun4, dfun3, interval, num_guesses, method='secant')
print_roots(roots, real_roots)
