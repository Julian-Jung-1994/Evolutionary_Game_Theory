import numpy as np


def constant_binary_distribution(types, rates, size_population):

    constant_binary_distribution_checks(types, rates, size_population)

    players = np.array([])
    for rate in enumerate(rates):
        tmp = [types[rate[0]]] * int(np.round(rate[1] * size_population))
        players = np.append(players, tmp)

    players = list(players)

    return players


# TODO in its own script -> create sub-directory for each module
def constant_binary_distribution_checks(types, rates, size_population):

    # rate checks
    rates_arr = np.array(rates)
    if not 0 <= rates_arr.any() <= 1:
        raise Exception('rates must be in range of [0, 1]')
    elif rates_arr.sum() != 1:
        raise Exception('population rates do not add up to 1')