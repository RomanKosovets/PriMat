import numpy as np
import matplotlib.pyplot as plt


def func1(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2      # Функция Бута


def df1_x(x, y):
    return 10 * x + 8 * y - 34


def df1_y(x, y):
    return 8 * x + 10 * y - 38


def func2(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2        # Функция Химмельблау


def df2_x(x, y):
    return 4 * x * (x**2 + y - 11) + 2 * (x + y**2 - 7)


def df2_y(x, y):
    return 2 * (x**2 + y - 11) + 4 * y * (x + y**2 - 7)


def makeGraph(title, a, b, f, x_list, y_list):
    X = np.arange(a, b, 0.1)
    Y = np.arange(a, b, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = f(X, Y)

    plt.rcParams["figure.figsize"] = (10, 15)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    ax.plot(x_list, y_list, f(np.array(x_list), np.array(y_list)), 'o-', c="red", markersize=5)
    ax.plot([x_list[-1]], [y_list[-1]], f(np.array(x_list[-1]), np.array(y_list[-1])), 'o', c="blue", markersize=8)
    plt.show()


def vanillaGradient(title, f, df_x, df_y, x0, y0, eps, alpha, a, b):
    x_list, y_list = [], []

    x_list.append(x0)
    y_list.append(y0)

    last_x, last_y = x0, y0
    curr_x = last_x - alpha * df_x(last_x, last_y)
    curr_y = last_y - alpha * df_y(last_x, last_y)
    counter = 1
    while abs(f(curr_x, curr_y) - f(last_x, last_y)) > eps:
        x_list.append(curr_x)
        y_list.append(curr_y)

        last_x, last_y = curr_x, curr_y
        curr_x = last_x - alpha * df_x(last_x, last_y)
        curr_y = last_y - alpha * df_y(last_x, last_y)
        counter += 1

    title = title + "\nConstant Step"
    makeGraph(title, a, b, f, x_list, y_list)

    print("Number of iterations:", counter)
    print("x:", curr_x)
    print("y:", curr_y, "\n")


title = "Function Booth: (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2"
print(title)
vanillaGradient(title, func1, df1_x, df1_y, -4, 1, 0.00001, 0.001, -4, 4)

title = "Function Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2 "
print(title)
vanillaGradient(title, func2, df2_x, df2_y, -2, 2, 0.00001, 0.001, -4, 4)
