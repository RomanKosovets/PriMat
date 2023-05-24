import numpy as np


def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        # Выбор ведущего элемента
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j, i]) > abs(A[max_row, i]):
                max_row = j
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Приведение матрицы к треугольному виду
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


# Пример использования
A = np.array([[2.0, 1.0, 0.0],
              [1.0, 3.0, 1.0],
              [0.0, 1.0, 4.0]])
b = np.array([1.0, 2.0, 3.0])

x = gauss_elimination(A, b)
print("Решение: ", x)
