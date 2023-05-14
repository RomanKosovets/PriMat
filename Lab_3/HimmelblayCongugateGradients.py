import numpy as np
import matplotlib.pyplot as plt
from GradientConstantStep import makeGraph

def himmelblau(x, y):
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


def himmelblau_gradient(x, y):
    df_dx = 4 * x * (x ** 2 + y - 11) + 2 * (x + y ** 2 - 7)
    df_dy = 2 * (x ** 2 + y - 11) + 4 * y * (x + y ** 2 - 7)
    return df_dx, df_dy


def conjugate_gradient(start_x, start_y, epsilon, max_iterations):
    x_list, y_list = [start_x], [start_y]
    x, y = start_x, start_y
    grad_x, grad_y = himmelblau_gradient(x, y)
    d_x, d_y = -grad_x, -grad_y
    alpha = 0.01
    for i in range(max_iterations):
        if np.sqrt(grad_x ** 2 + grad_y ** 2) < epsilon:
            break
        x_list.append(x)
        y_list.append(y)
        alpha = 0.01
        while himmelblau(x + alpha * d_x, y + alpha * d_y) >= himmelblau(x, y):
            alpha *= 0.5
        x += alpha * d_x
        y += alpha * d_y
        grad_x_new, grad_y_new = himmelblau_gradient(x, y)
        beta = (grad_x_new ** 2 + grad_y_new ** 2) / (grad_x ** 2 + grad_y ** 2)
        d_x = -grad_x_new + beta * d_x
        d_y = -grad_y_new + beta * d_y
        grad_x, grad_y = grad_x_new, grad_y_new
    return x_list, y_list, x, y


# Задаем начальные значения и точность
start_x = -4
start_y = 4
epsilon = 0.00001
max_iterations = 1000

# Выполняем оптимизацию сопряженными градиентами
x_list, y_list, min_x, min_y = conjugate_gradient(start_x, start_y, epsilon, max_iterations)

# Выводим результаты
print("Number of iterations:", len(x_list))
print("Minimum x:", min_x)
print("Minimum y:", min_y)

# Строим график с пошаговым движением к минимуму функции
makeGraph("Himmelblau Function", -4, 4, himmelblau, x_list, y_list)

