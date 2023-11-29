import typing
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

ergodic_markov_chain = np.array([
    np.array([0.1, 0.3, 0, 0, 0.6, 0, 0, 0], dtype=float),
    np.array([0.4, 0.1, 0, 0, 0.2, 0.1, 0.2, 0], dtype=float),
    np.array([0, 0.1, 0.2, 0, 0, 0, 0.7, 0], dtype=float),
    np.array([0, 0, 0, 0.1, 0, 0, 0.4, 0.5], dtype=float),
    np.array([0.1, 0.2, 0, 0, 0.5, 0.2, 0, 0], dtype=float),
    np.array([0, 0.1, 0, 0, 0.1, 0.2, 0.6, 0], dtype=float),
    np.array([0, 0, 0.2, 0.2, 0, 0.3, 0.1, 0.2], dtype=float),
    np.array([0, 0, 0, 0.2, 0, 0, 0.5, 0.3], dtype=float),
])

initial_states = np.array([
    np.array([1, 0, 0, 0, 0, 0, 0, 0], dtype=float),
    np.array([0, 1, 0, 0, 0, 0, 0, 0], dtype=float),
])

different_steps = np.array([5, 10, 50])

# графическое представление марковской цепи
def show_chain(chain: np.ndarray[np.ndarray[float]],vx_names: np.ndarray[str]):
    g = nx.DiGraph()
    for i, row in enumerate(chain):
        for j, val in enumerate(row):
            if val <= 0:
                continue

            g.add_edge(vx_names[i], vx_names[j], weight=val)

    pos = nx.circular_layout(g)
    nx.draw_networkx_nodes(g, pos, node_size=200, node_color='black')
    nx.draw_networkx_labels(g, pos, font_size=7, font_color='white')
    nx.draw_networkx_edges(g, pos, width=1, edge_color='black')
    nx.draw_networkx_edge_labels(g, pos, nx.get_edge_attributes(g, 'weight'), font_size=6)
    plt.show()

# Функция для построения графика стандартных отклонений на каждом шаге для различных начальных состояний
def plot_std(eps: float = 1e-6, *args):
    for std in args:
        plt.plot(np.arange(std.shape[0]), std)

    plt.xlabel('Steps')
    plt.ylabel('Std')
    plt.title(f'Std of state distribution. Eps: {eps}')
    plt.show()

# Функция для вычисления распределения состояний цепи численным методом
def state_dist_numeric(chain: np.ndarray[np.ndarray[float]], initial_state: np.ndarray[float],
                       eps: float = 1e-6, steps: int = 1000) -> typing.Tuple[np.ndarray[float], np.ndarray[float]]:
    std = np.array([np.std(initial_state)])
    while steps > 0:
        initial_state = np.matmul(initial_state, chain)
        cur_std = np.std(initial_state)
        if np.abs(std[-1] - cur_std) < eps:
            break

        std = np.append(std, cur_std)
        steps -= 1

    return initial_state, std


# Функция для вычисления распределения состояний цепи аналитическим методом
def state_dist_analitic(transition_matrix):
    equations = transition_matrix.transpose()
    equations -= np.identity(equations.shape[0])

    last_equation = np.ones((1, equations.shape[1]))
    equations = np.append(equations, last_equation, axis=0)

    ordinate = np.zeros(equations.shape[0])
    ordinate[-1] = 1

    probability_vec = np.linalg.lstsq(equations, ordinate, rcond=None)[0]

    return probability_vec


if __name__ == '__main__':

    np.set_printoptions(precision=3, suppress=True)
    show_chain(ergodic_markov_chain, np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))
    stds = []
    print('Numeric:')

    for step in different_steps:
        for initial_state in initial_states:
            state, std = state_dist_numeric(ergodic_markov_chain, initial_state, steps=step)
            print(f'State distribution after {step} steps: {state},')
            stds.append(std)

    plot_std(1e-6, *stds)
    print(f'\nAnalytic:\n{state_dist_analitic(ergodic_markov_chain)}')