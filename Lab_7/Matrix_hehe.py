import numpy as np

ergodic_markov_chain = np.array([
    np.array([0.093, 0.043, 0.196, 0.165, 0.208, 0.108, 0.043, 0.144], dtype=float),
    np.array([0.103, 0.118, 0.097, 0.144, 0.096, 0.109, 0.186, 0.147], dtype=float),
    np.array([0.127, 0.135, 0.129, 0.148, 0.099, 0.141, 0.069, 0.152], dtype=float),
    np.array([0.114, 0.098, 0.195, 0.142, 0.265, 0.088, 0.047, 0.051], dtype=float),
    np.array([0.149, 0.18,  0.000, 0.053, 0.168, 0.001, 0.211, 0.238], dtype=float),
    np.array([0.17 , 0.107, 0.119, 0.077, 0.067, 0.142, 0.136 ,0.182], dtype=float),
    np.array([0.148, 0.141, 0.081, 0.193, 0.091, 0.199, 0.113, 0.034], dtype=float),
    np.array([0.096, 0.178, 0.183, 0.078, 0.006, 0.212, 0.195, 0.052], dtype=float),
])
def create_random_matrix(rows, cols):
    # Генерируем случайную матрицу размером (rows, cols) с элементами от 0 до 1
    random_matrix = np.random.rand(rows, cols)

    # Нормализуем сумму по каждой строке
    normalized_matrix = random_matrix / random_matrix.sum(axis=1, keepdims=True)

    # Нормализуем сумму по каждому столбцу
    normalized_matrix /= normalized_matrix.sum(axis=0, keepdims=True)

    return normalized_matrix

# Устанавливаем ограничение на количество знаков после запятой
np.set_printoptions(precision=3)

# Пример использования
rows = 8
cols = 8
random_result_matrix = create_random_matrix(rows, cols)

print("Созданная случайная матрица:")
print(random_result_matrix)
print("Сумма элементов по строкам:", np.sum(ergodic_markov_chain, axis=1))
print("Сумма элементов по столбцам:", np.sum(ergodic_markov_chain, axis=0))
