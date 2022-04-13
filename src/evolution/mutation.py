import numpy as np


def binary_uncorrelated(types, replications, size_population, mutation_rate):

    # rates to player
    players = np.array([])
    for rate in enumerate(replications):
        tmp = [types[rate[0]]] * int(np.round(rate[1] * size_population))
        players = np.append(players, tmp)

    induce_mutation = np.random.choice(2, size_population, p=[1 - mutation_rate, mutation_rate])

    # mutations TODO numpy methods should exist that are more efficient than looping
    for i in range(len(induce_mutation)):
        if induce_mutation[i] == 1:
            players[i] = abs(players[i] - 1)

    # player to rates
    rate_dove = sum(np.isin(players, 0)) / size_population
    rate_hawk = sum(np.isin(players, 1)) / size_population
    replications = [rate_dove, rate_hawk]

    return replications
