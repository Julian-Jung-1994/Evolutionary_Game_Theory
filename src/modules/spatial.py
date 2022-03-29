import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def space_definition(rows=50, columns=50):

    space = np.zeros([rows, columns])

    return space


def players_in_space(space, players):

    # find shape of space. basis for place randomizer
    rows = space.shape[0]
    columns = space.shape[1]

    # find position for each player: bring to space and collect in list
    space_player = space.copy()
    positions = []
    for i in range(len(players)):
        position = (np.random.randint(rows), np.random.randint(columns))
        space_player[position[0], position[1]] += 1
        positions.append([players[i], position])

    return space_player, positions


def diagram_player_space(space_player):

    sns.heatmap(space_player)
    plt.show()
