import math as m

a = -2.45
b = 2.45
epsilon = 0.0000001
steps = 1
phi = (m.sqrt(5) - 1) / 2


def f(x):
    return m.sin(x) * m.pow(x, 3)


def CalcDistance(a, b):
    return phi * (b - a)


x1 = b - CalcDistance(a, b)
x2 = a + CalcDistance(a, b)

fx1 = f(x1)
fx2 = f(x2)

while (b - a) > epsilon:
    if fx1 > fx2:
        a = x1
        x1 = x2
        fx1 = fx2
        x2 = a + CalcDistance(a, b)
        fx2 = f(x2)
    else:
        b = x2
        x2 = x1
        fx2 = fx1
        x1 = b - CalcDistance(a, b)
        fx1 = f(x1)

    steps += 1

print("Самая глубокая точка", (b + a) / 2)
print("Кол-во итераций", steps)
