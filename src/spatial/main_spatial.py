from src.spatial.player import player as pl
from src.spatial.grid import initial_grid as gr
from src.spatial.diagram import grid_diagram as dia


def spatial(types=[1, 2], rates=[0.5, 0.5], size_population=10,
            rows=10, columns=10,
            institutions=[[[1, 3], [2, 6]]]):

    # collection lists
    players = []
    grid = []
    distribution = []

    # initial values
    players_init = pl.player_distribution(types=types, rates=rates, size_population=size_population)
    grid_distribution_init = gr.grid_start(rows=rows, columns=columns, players=players_init)

    players.append(players_init)
    grid.append(grid_distribution_init[0])
    distribution.append(grid_distribution_init[1])

    dia.institution_grid(grid[0], institutions)

    return players, grid, distribution
