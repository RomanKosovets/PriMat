import math as m

a = -2.45
b = 2.45
epsilon = 0.0000001


def f(x):
    return m.sin(x) * m.pow(x, 3)


def fibonacci(n):
    x = 0
    y = 1
    while n > 1:
        z = x + y
        x = y
        y = z
        n -= 1
    return x + y


def golden_section(f, a, b, epsilon):
    k = (b - a) / epsilon
    n = 1
    while fibonacci(n + 1) <= k:
        n += 1
    steps = n + 1

    x1 = a + (b - a) * fibonacci(n - 1) / fibonacci(n + 1)
    x2 = a + (b - a) * fibonacci(n) / fibonacci(n + 1)
    f1 = f(x1)
    f2 = f(x2)

    for i in range(1, n - 1):
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (b - a) * fibonacci(n - i - 1) / fibonacci(n - i)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) * fibonacci(n - i) / fibonacci(n - i + 1)
            f2 = f(x2)
    return (a + b) / 2, steps


x_min, steps = golden_section(f, a, b, epsilon)
print("Минимум функции y=sin(x)*x^3 на интервале [ {}, {} ] равен {}".format(a, b, x_min))
print("Кол-во итераций:", steps)

