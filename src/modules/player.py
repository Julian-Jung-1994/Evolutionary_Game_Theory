import numpy as np
from src.checks import player as check


def player_distribution(types, rates, size_population):

    check.constant_binary_distribution_checks(types, rates, size_population)

    players = np.array([])
    for rate in enumerate(rates):
        tmp = [types[rate[0]]] * int(np.round(rate[1] * size_population))
        players = np.append(players, tmp)

    players = list(players)

    return players
