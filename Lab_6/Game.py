import numpy as np
import json
from operator import add, neg


def read_matrix_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        matrix = np.array(data['matrix'])
    return matrix


def find_dominant_strategies(matrix, flag):
    dominant_row_strategies = None
    dominant_column_strategies = None
    row_max = np.min(matrix, axis=1)
    column_min = np.max(matrix, axis=0)

    if row_max.max() == column_min.min():
        dominant_row_strategies = np.where(row_max == row_max.max())[0]
        dominant_column_strategies = np.where(column_min == column_min.min())[0]
    else:
        flag = False

    return dominant_row_strategies, dominant_column_strategies, flag


def remove_superior_rows(matrix, flag_player):
    rows_to_remove = []
    for i in range(len(matrix)):
        is_superior = True
        for j in range(len(matrix)):
            if i != j and all(matrix[i] > matrix[j]) and flag_player:
                is_superior = False
                break
            elif i != j and all(matrix[i] < matrix[j]) and not flag_player:
                is_superior = False
                break
        if not is_superior:
            rows_to_remove.append(j)

    reduced_matrix = np.delete(matrix, rows_to_remove, axis=0)
    return reduced_matrix


def findMixedStrategies(payoff_matrix, iterations=1000000):
    transpose = list(zip(*payoff_matrix))
    # Определяем количество строк и столбцов в матрице выигрышей
    numrows = len(payoff_matrix)
    numcols = len(transpose)

    row_cum_payoff = [0] * numrows
    col_cum_payoff = [0] * numcols
    colpos = range(numcols)
    rowpos = map(neg, range(numrows))
    colcnt = [0] * numcols
    rowcnt = [0] * numrows
    active = 0
    for i in range(iterations):
        rowcnt[active] += 1
        col_cum_payoff = list(map(add, payoff_matrix[active], col_cum_payoff))
        active = -1
        min_col_cum_payoff = min(col_cum_payoff, default=None)
        if min_col_cum_payoff is not None:
            active = col_cum_payoff.index(min_col_cum_payoff)
        if active == -1:
            break
        colcnt[active] += 1
        row_cum_payoff = list(map(add, transpose[active], row_cum_payoff))
        active = -1
        max_row_cum_payoff = max(row_cum_payoff, default=None)
        if max_row_cum_payoff is not None:
            active = row_cum_payoff.index(max_row_cum_payoff)
        if active == -1:
            break
    value_of_game = (max(row_cum_payoff) + min(col_cum_payoff)) / 2.0 / iterations
    for i in range(len(rowcnt)):
        rowcnt[i] = rowcnt[i] / iterations
    for i in range(len(colcnt)):
        colcnt[i] = colcnt[i] / iterations

    return rowcnt, colcnt, value_of_game


if __name__ == '__main__':
    file_path = 'game_matrix.json'
    game_matrix = read_matrix_from_json(file_path)
    print("Исходная платежная матрица игры:")
    print(game_matrix)

    flag_clean_or_mixed_stratagy = True
    dominant_row_strategies, dominant_column_strategies, flag_clean_or_mixed_stratagy = find_dominant_strategies(game_matrix, flag_clean_or_mixed_stratagy)

    if flag_clean_or_mixed_stratagy:
        print("\nСедловая точка имеет индекс: (", dominant_row_strategies[0] + 1,
              ",", dominant_column_strategies[0] + 1, ")")
        print("Цена игры, если есть седловая точка:", game_matrix[dominant_row_strategies, dominant_column_strategies][0])
    else:
        flag_player = True  # True для первого игрока
        reduced_matrix = remove_superior_rows(game_matrix, flag_player)

        flag_player = False  # False для второго игрока
        reduced_matrix_tr = np.transpose(reduced_matrix)
        reduced_matrix_tr = np.transpose(remove_superior_rows(reduced_matrix_tr, flag_player))

        print("\nУменьшенная матрица игры после убирания доминантных строк:")
        print(reduced_matrix_tr)

        print("\nЗначение цены игры в смешанных стратегиях:")
        find_price_matrix = findMixedStrategies(reduced_matrix_tr)
        print(find_price_matrix)




# "matrix": [
#     [-5, 3, 1, 20],
#     [5, 5, 4, 6],
#     [-4, -2, 0, -5]
# ]
#   "matrix": [
#     [1, 7, 4],
#     [8, 3, 9],
#     [3, 1, 4]
#   ]