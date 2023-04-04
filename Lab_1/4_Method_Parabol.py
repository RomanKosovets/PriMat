import math as m


def f(x):
    return x ** 2 # m.sin(x) * m.pow(x, 3)


a = -2.45
b = 2.45
epsilon = 1e-7
steps = 1

x1 = a
x2 = (a + b) / 2
x3 = b

while True:

    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)

    u = x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) / (
            2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1)))

    if abs(x2 - u) < epsilon:
        print("Минимум:", (x2 + u) / 2)
        print("Кол-во итераций:", steps)
        break

    fu = f(u)

    if u > x2:
        if fu < f2:
            x1 = x2
            x2 = u
        else:
            x3 = u
    else:
        if fu < f2:
            x3 = x2
            x2 = u
        else:
            x1 = u
    steps += 1