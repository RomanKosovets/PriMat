import numpy as np
from Lab_4.GaussPrincipalComponent import gauss_elimination


# функция для генерации матрицы Гильберта с заданным числом обусловленности
def hilbert_matrix(n, k):
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1 / (i + j + k + 1)
    return H


# функция для решения СЛАУ методом Якоби
def jacobi_iteration(A, b, x0, max_iter=1000, tol=1e-6):
    n = len(A)
    D = np.diag(A)
    R = A - np.diag(D)
    x = x0.copy()
    for k in range(max_iter):
        x_prev = x.copy()
        x = (b - np.dot(R, x)) / D
        if np.linalg.norm(x - x_prev) < tol:
            break
    return x


for k in [1, 10, 100, 1000]:
    H = hilbert_matrix(5, k)
    b = np.ones(5)
    # решение методом Гаусса
    x_gauss = gauss_elimination(H, b)
    # решение методом Якоби
    x_jacobi = jacobi_iteration(H, b, np.zeros(5))
    print(f"Число обусловленности: {np.linalg.cond(H)}")
    print(f"Решение методом Гаусса: {x_gauss}")
    print(f"Решение методом Якоби: {x_jacobi}\n")
