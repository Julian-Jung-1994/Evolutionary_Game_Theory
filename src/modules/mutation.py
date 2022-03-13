import numpy as np


def binary_uncorrelated(types, replications, size_population, mutation_rate):

    # rates to player
    players = np.array([])
    for rate in enumerate(replications):
        tmp = [types[rate[0]]] * int(np.round(rate[1] * size_population))
        players = np.append(players, tmp)

    induce_mutation = np.random.choice(2, size_population, p=[1 - mutation_rate, mutation_rate])

    # mutations TODO numpy methods should exist that are more efficient than looping
    mutated_players = np.array([])
    for x in zip(players, induce_mutation):
        if x[1] == 0:
            mutated_players = np.append(mutated_players, x[0])
        else:
            mutated_players = np.append(mutated_players, abs(x[1]-1))

    # player to rates
    rate_dove = sum(np.isin(mutated_players, 0)) / size_population
    rate_hawk = sum(np.isin(mutated_players, 1)) / size_population
    replications = [rate_dove, rate_hawk]
    print(replications)
    return replications
