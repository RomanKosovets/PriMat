import numpy as np

def generate_quadratic_function(n, k):
    # Генерируем случайную матрицу A размера n x n
    A = np.random.rand(n, n)

    # Делаем A симметричной путем складывания с транспонированной копией без диагонали
    A = A + A.T - np.diag(A.diagonal())

    # Вычисляем сингулярное разложение матрицы A
    U, S, V = np.linalg.svd(A)

    # Определяем диагональную матрицу Sigma
    Sigma = np.diag(S)

    # Определяем матрицу B с числом обусловленности k
    B = U @ np.diag(np.linspace(1, k, n)) @ V

    # Генерируем случайный вектор c размера n
    c = np.random.rand(n)

    # Генерируем случайное смещение d
    d = np.random.rand()

    # Формируем квадратичную функцию в виде f(x) = x^T * B * x + c^T * x + d
    def quadratic_function(x):
        return x.T @ B @ x + c.T @ x + d

    return quadratic_function

def quadratic_function_to_string(quadratic_function, n):
    variables = [f'x{i+1}' for i in range(n)]
    terms = []
    for i in range(n):
        for j in range(i, n):
            term = f"{variables[i]}^{variables[j]}"
            if i != j:
                term += f" + {variables[j]}^{variables[i]}"
            terms.append(term)
    quadratic_str = ' + '.join(terms)
    quadratic_str += ' + c'  # Adding the constant term
    return quadratic_str



n = 2  # Number of variables
k = 10  # Condition number

quadratic_function = generate_quadratic_function(n, k)
quadratic_str = quadratic_function_to_string(quadratic_function, n)

print(quadratic_str)