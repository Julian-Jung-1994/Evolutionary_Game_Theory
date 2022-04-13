import numpy as np


def grid_start(rows=10, columns=10, players=[1, 1, 1, 1, 1, 2, 2, 2, 2, 2]):

    grid = np.array(empty_rectangle(rows, columns))
    xs = []
    ys = []

    rows = len(grid)
    cols = len(grid[0])

    positions = [(i, j) for i in range(rows) for j in range(cols)]
    for player in players:
        index = np.random.randint(100)
        coordinates = positions[index]
        x = coordinates[0]
        y = coordinates[1]

        grid[x][y] = player
        xs.append(x)
        ys.append(y)

    starting_grid = grid.tolist()
    grid_collector = [players, xs, ys]

    return starting_grid, grid_collector


def empty_rectangle(rows=10, columns=10):

    starting_rectangle = []
    grid_cols = [0] * columns

    for row in range(rows):
        starting_rectangle.append(grid_cols)

    return starting_rectangle
