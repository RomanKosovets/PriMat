import math as m

a = -2.45
b = 2.45
epsilon = 0.0000001
alpha = epsilon / 2
steps = 1


def f(x):
    func = m.sin(x) * m.pow(x, 3)
    return func


while (b - a) / 2 > epsilon:
    mid = (a + b) / 2
    c = mid - alpha
    d = mid + alpha

    if f(c) > f(d):
        a = c
    else:
        b = d
    steps += 1

print("самая глубокая точка =", mid)
print("Количество итераций =", steps)

