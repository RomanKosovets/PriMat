import numpy as np


def jacobi_method(A, b, max_iterations=100, tolerance=1e-8):
    n = A.shape[0]

    # Выполняем разложение матрицы A = D + L + U
    D = np.diag(np.diag(A))
    L = -np.tril(A, k=-1)
    U = -np.triu(A, k=1)

    # Инициализируем вектор приближенных решений x
    x = np.zeros_like(b)

    # Итерационный процесс метода Якоби
    for _ in range(max_iterations):
        x_new = np.linalg.inv(D).dot(b + L.dot(x) + U.dot(x))
        if np.allclose(x, x_new, rtol=tolerance):
            break
        x = x_new

    return x


# Генерируем матрицу (3x3)
A = np.array([
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4]
])

# Генерируем вектор правой части уравнений
b = np.array([2, 3, 5])

# Выполняем метод Якоби для решения СЛАУ
solution = jacobi_method(A, b)

# Выводим решение
print("Решение: ", solution)