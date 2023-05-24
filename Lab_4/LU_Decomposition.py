import numpy as np


def lu_decomposition(A):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros_like(A)

    for i in range(n):
        U[i, i:] = A[i, i:] - L[i, :i] @ U[:i, i:]
        L[i + 1:, i] = (A[i + 1:, i] - L[i + 1:, :i] @ U[:i, i]) / U[i, i]

    return L, U


def lu_solve(L, U, b):
    n = L.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)

    # Решение Ly = b (прямой ход)
    for i in range(n):
        y[i] = b[i] - L[i, :i] @ y[:i]

    # Решение Ux = y (обратный ход)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]

    return x


# Исходная матрица системы
A = np.array([[2.0, 1.0, 0.0],
              [1.0, 3.0, 1.0],
              [0.0, 1.0, 4.0]])

# Вектор правой части
b = np.array([1.0, 2.0, 3.0])

# Выполнение LU-разложения
L, U = lu_decomposition(A)

# Решение системы уравнений
x = lu_solve(L, U, b)

# Вывод результата
print("Решение: ", x)
