import matplotlib.pyplot as plt
from GradientConstantStep import makeGraph
from GradientConstantStep import func1, func2, df1_x, df1_y, df2_x, df2_y

plt.rcParams["figure.figsize"] = (10, 15)


def gradientArmijo(title, f, df_x, df_y, x0, y0, eps, alpha, a, b):
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
        if f(curr_x, curr_y) > f(last_x, last_y):
            alpha *= 0.5
        curr_x = last_x - alpha * df_x(last_x, last_y)
        curr_y = last_y - alpha * df_y(last_x, last_y)
        counter += 1

    title = title + "\nCrushed Step"
    makeGraph(title, a, b, f, x_list, y_list)

    print("Number of iterations:", counter)
    print("x:", curr_x)
    print("y:", curr_y, "\n")


title = "Function: x^2 + y^2 - xy"
print(title)
gradientArmijo(title, func1, df1_x, df1_y, 5, 8, 0.00001, 0.1, -10, 10)


title = "Function Himmelblau: (x**2 + y - 11)**2 + (x + y**2 - 7)**2 "
print(title)
gradientArmijo(title, func2, df2_x, df2_y, -2, 2, 0.00001, 0.001, -4, 4)
