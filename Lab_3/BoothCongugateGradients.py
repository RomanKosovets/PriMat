# Задаем функцию Бута
import numpy as np
from GradientConstantStep import makeGraph


def booth(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2


# Задаем градиент функции Бута
def booth_gradient(x, y):
    df_dx = 2 * (x + 2 * y - 7) + 4 * (2 * x + y - 5)
    df_dy = 4 * (x + 2 * y - 7) + 2 * (2 * x + y - 5)
    return df_dx, df_dy


# Функция для выполнения оптимизации сопряженными градиентами для функции Бута
def conjugate_gradient_booth(start_x, start_y, epsilon, max_iterations):
    x_list, y_list = [start_x], [start_y]
    x, y = start_x, start_y
    grad_x, grad_y = booth_gradient(x, y)
    d_x, d_y = -grad_x, -grad_y
    alpha = 0.01
    for _ in range(max_iterations):
        if np.sqrt(grad_x ** 2 + grad_y ** 2) < epsilon:
            break
        x_list.append(x)
        y_list.append(y)
        alpha = 0.01
        while booth(x + alpha * d_x, y + alpha * d_y) >= booth(x, y):
            alpha *= 0.5
        x += alpha * d_x
        y += alpha * d_y
        grad_x_new, grad_y_new = booth_gradient(x, y)
        beta = (grad_x_new ** 2 + grad_y_new ** 2) / (grad_x ** 2 + grad_y ** 2)
        d_x = -grad_x_new + beta * d_x
        d_y = -grad_y_new + beta * d_y
        grad_x, grad_y = grad_x_new, grad_y_new
    return x_list, y_list, x, y


# Задаем начальные значения и точность
start_x = -4
start_y = 1
epsilon = 0.001
max_iterations = 1000

# Выполняем оптимизацию сопряженными градиентами для функции Бута
x_list, y_list, min_x, min_y = conjugate_gradient_booth(start_x, start_y, epsilon, max_iterations)

# Выводим результаты
print("Number of iterations:", len(x_list))
print("Minimum x:", min_x)
print("Minimum y:", min_y)

# Строим график с пошаговым движением к минимуму функции Бута
title = "Function Booth: (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2"
makeGraph(title, -4, 4, booth, x_list, y_list)
