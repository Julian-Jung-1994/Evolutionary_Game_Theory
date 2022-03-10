import numpy as np


def constant_binary_distribution(rates, size_population):
    """
    from rates and the size of population, a list with each entity included is created

    Parameters
    ----------
    rates : list of floats - two entries
        population rates as entries.
    size_population : int
        total size of population

    Returns
    -------
    players : list of floats
        list with each player represented
    """

    if sum(rates) != 1:
        raise Exception('population rates do not add up to 1')

    players = np.array([])
    for rate in enumerate(rates):
        tmp = [rate[0]] * int(np.round(rate[1] * size_population))
        players = np.append(players, tmp)

    players = list(players)

    return players
