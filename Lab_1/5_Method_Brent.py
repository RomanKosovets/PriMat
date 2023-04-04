import math as m


def func(x):
    return m.sin(x) * x ** 3


def brent(a, b, epsilon=1e-7, steps=1):
    GoldRatio = (3 - m.sqrt(5)) / 2  # Константа для метода золотого сечения
    x = w = v = a + GoldRatio * (b - a)
    fx = fw = fv = func(x)
    d = e = b - a
    while True:

        xm = 0.5 * (a + b)  # mid
        epsilon2 = 2 * epsilon

        if abs(x - xm) <= epsilon2:
            return x, steps

        if abs(e) > epsilon:

            r = (x - w) * (fx - fv)
            q = (x - v) * (fx - fw)
            p = (x - v) * q - (x - w) * r
            q = 2 * (q - r)

            if q > 0:
                p = -p

            Etemp = e
            e = d

            if abs(p) >= abs(0.5 * q * Etemp):
                if x < xm:
                    e = b - x
                else:
                    e = a - x

                d = GoldRatio * e
            else:
                d = p / q
                u = x + d
                if u - a < epsilon2 or b - u < epsilon2:
                    if x < xm:
                        d = epsilon
                    else:
                        d = -epsilon
        if abs(d) >= epsilon:
            u = x + d
        elif d > 0:
            u = x + epsilon
        else:
            u = x - epsilon

        fu = func(u)

        if fu <= fx:
            if u >= x:
                a = x
            else:
                b = x
            v, fv = w, fw
            w, fw = x, fx
            x, fx = u, fu
        else:
            if u >= x:
                b = u
            else:
                a = u

            if fu <= fw or w == x:
                v, fv = w, fw
                w, fw = u, fu
            elif fu <= fv or v == x or v == w:
                v, fv = u, fu
        steps += 1


x, steps = brent(-2.45, 2.45)
print("Минимум:", x)
print("Количество итераций:", steps)
