import scipy.optimize as opt
import math

def func(x):
    return math.sin(x) * x ** 3

res = opt.minimize_scalar(func, bracket=(-2.45, 0, 2.45), method='Brent')
print("Минимум функции:", res.fun)
print("Аргумент минимума:", res.x)