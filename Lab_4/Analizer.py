import numpy as np
import time

from Lab_4.JacobiMethod import jacobi_method


def generate_matrix_A(n, diagonal_dominance):
    # Генерируем случайную матрицу A с заданным уровнем диагонального преобладания
    A = np.random.choice([-4, -3, -2, -1, 0], size=(n, n))
    np.fill_diagonal(A, diagonal_dominance * np.abs(A).sum(axis=1))
    return A


def generate_vector_b(n):
    # Генерируем случайный вектор правой части b
    return np.random.rand(n)


def exact_solution(A, b):
    # Вычисляем точное решение (если известно)
    return np.linalg.solve(A, b)


def compare_solutions(solution1, solution2):
    # Сравниваем два решения и оцениваем точность
    return np.allclose(solution1, solution2)


# Параметры исследования
n = 3  # Размерность матрицы
num_tests = 10  # Количество тестовых случаев
max_iterations = 100  # Максимальное число итераций метода Якоби
tolerance = 1e-8  # Точность решения метода Якоби

# Результаты исследования
jacobi_accuracy = []  # Точность решения метода Якоби
jacobi_speed = []  # Время выполнения метода Якоби
lu_accuracy = []  # Точность решения LU-разложения
lu_speed = []  # Время выполнения LU-разложения

for _ in range(num_tests):
    # Генерируем матрицу A с разным уровнем диагонального преобладания
    diagonal_dominance = np.random.uniform(0.1, 10)
    A = generate_matrix_A(n, diagonal_dominance)

    # Генерируем вектор правой части b
    b = generate_vector_b(n)

    # Решение методом Якоби
    start_time = time.time()
    jacobi_solution = jacobi_method(A, b, max_iterations, tolerance)
    end_time = time.time()
    jacobi_speed.append(end_time - start_time)

    # Решение с помощью LU-разложения
    start_time = time.time()
    lu_solution = np.linalg.solve(A, b)
    end_time = time.time()
    lu_speed.append(end_time - start_time)

    # Вычисляем точное решение (если известно)
    exact_sol = exact_solution(A, b)

    # Сравниваем решения и оцениваем точность
    jacobi_accuracy.append(compare_solutions(jacobi_solution, exact_sol))
    lu_accuracy.append(compare_solutions(lu_solution, exact_sol))

# Вывод результатов
print("Метод Якоби:")
print("Средняя точность: ", np.mean(jacobi_accuracy))
print("Среднее время выполнения: ", np.mean(jacobi_speed))
print("\nLU-разложение:")
print("Средняя точность: ", np.mean(lu_accuracy))
print("Среднее время выполнения: ", np.mean(lu_speed))

