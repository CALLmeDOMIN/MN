from numpy import log10 as np_log10, cosh as np_cosh, exp as np_exp, sin as np_sin, sqrt as np_sqrt, isclose as np_isclose, abs as np_abs, linspace as np_linspace, inf as np_inf, isfinite as np_isfinite

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        return None, None
    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c, i
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, i


def false_position_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        return None, None
    for i in range(max_iter):
        if np_isclose(f(b) - f(a), 0, atol=tol):
            return None, None
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if not np_isfinite(f(c)):
            return None, None
        if np_abs(f(c)) < tol:
            return c, i
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a * f(b) - b * f(a)) / (f(b) - f(a)), i


def find_roots(f, a, b, tol=1e-6, max_iter=1000, method=bisection_method):
    roots = []
    intervals = np_linspace(a, b, max_iter)
    for i in range(len(intervals) - 1):
        a = intervals[i]
        b = intervals[i + 1]
        if f(a) * f(b) <= 0:
            try:
                root, iterations = method(f, a, b, tol, max_iter)
                if root is not None:
                    roots.append((root, iterations))
            except (ZeroDivisionError, ValueError):
                pass
    return roots

def is_real_root(found_root, real_roots, tol=1e-6):
    return any(abs(found_root - real_root) < tol for real_root in real_roots)


def find_and_check_roots(f, a, b, real_roots, tol=1e-6, max_iter=100, method=bisection_method):
    roots = find_roots(f, a, b, tol, max_iter, method)
    real_roots_found = []
    real_roots_iterations = []
    for root, iterations in roots:
        if is_real_root(root, real_roots, tol):
            real_roots_found.append(root)
            real_roots_iterations.append(iterations)
    return real_roots_found, real_roots_iterations

def print_roots(roots, iterations):
    if len(roots) == 0:
        print("No real roots found")
    else:
        for i in range(len(roots)):
            print(f"Root: {roots[i]}, Iterations: {iterations[i]}")


def f1(x):
    if x == 0:
        return np_inf
    else:
        return np_log10(x ** 2 + 1) - x ** 3


def f2(x):
    if x == 0:
        return np_inf
    else:
        return np_cosh(x) - np_sqrt(x)


def f3(x):
    if x == 0:
        return np_inf
    else:
        return np_exp(-x) + np_sin(x) - 1 / x ** 2


start, end = 1e-6, 7

real_roots1 = [0.402505121796887]
real_roots2 = []
real_roots3 = [0.664813174227518566941017070, 3.13422699566592059290424701, 6.29395990811660257022381935]


print_roots(*find_and_check_roots(
    f1, start, end, real_roots1))

print_roots(*find_and_check_roots(
    f2, start, end, real_roots2))

print_roots(*find_and_check_roots(
    f3, start, end, real_roots3))

print_roots(*find_and_check_roots(
    f1, start, end, real_roots1, method=false_position_method))

print_roots(*find_and_check_roots(
    f2, start, end, real_roots2, method=false_position_method))

print_roots(*find_and_check_roots(
    f3, start, end, real_roots3, method=false_position_method))
