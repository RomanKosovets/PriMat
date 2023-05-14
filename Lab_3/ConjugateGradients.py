import numpy as np
import matplotlib.pyplot as plt
from Lab_3.GradientConstantStep import makeGraph
from Lab_3.GradientConstantStep import func1, func2, df1_x, df1_y, df2_x, df2_y

plt.rcParams["figure.figsize"] = (10, 15)


def conjugate_grad(title, f, a, b, matrix, free_vector, xy, eps):
    x_list, y_list = [], []
    x_list.append(xy[0])
    y_list.append(xy[1])
    grad = np.dot(matrix, xy) + free_vector
    pk = -grad
    xy_k = xy
    grad_norm = np.amax(np.abs(grad))
    counter = 0
    while grad_norm > eps:
        alpha_k = - np.dot(grad, pk) / np.dot(np.dot(pk, matrix.T), pk)
        xy_k = xy_k + alpha_k * pk
        grad_k = np.dot(matrix, xy_k) + free_vector
        beta_k = max(0, np.dot(grad_k, grad_k) / np.dot(grad, grad))
        pk = -grad_k + beta_k * pk
        grad = grad_k
        grad_norm = np.amax(abs(grad))
        x_list.append(xy_k[0])
        y_list.append(xy_k[1])
        counter += 1

    title = title + "\nConjugate gradient"
    makeGraph(title, a, b, f, x_list, y_list)

    print("Number of iterations:", counter)
    print("x:", xy_k[0])
    print("y:", xy_k[1], "\n")


title = "Function: x^2 + y^2 - xy"
print(title)
conjugate_grad(title, func1, -10, 10, np.array([[2, -1], [-1, 2]]), [0, 0], [5, 8], 0.00001)

title = "Function:  x^2 + 1/2*y^2 - yx + 4y"
print(title)
conjugate_grad(title, func2, -18, 18, np.array([[2, -1], [-1, 1]]), [0, 4], [-15, 15], 0.00001)
