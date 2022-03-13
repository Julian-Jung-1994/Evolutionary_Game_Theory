from src.modules import player, strategy, matching, replication, mutation, diagrams
import numpy as np


def population_ratio(
        game='hawk_dove', types=[0, 1], rates=[0.4, 0.6], match='random', mutation_rate=0.1,
        size_population=100, periods=100
):
    """
    as of now, two type hawk-dove game.

    Parameters
    ----------
    game : str
        {}
        future: name of predefined string, or replication matrix as input
    types : list of float
        i) for each entry in [0,1].
        players' types
    rates : list of float
        i) for each entry in [0,1]; ii) sum of all entries = 1; iii) length of types list
        population rates as entries
    match : str
        {}
        type of matching algorithm
    mutation_rate : list of float
        i) for each entry in [0,1]; ii) length of types list
        rate of mutation
    size_population : int
        total size of population
    periods : int
        number of repetitions the game is played

    Returns
    -------
    population_rate : list of float
        the population ratio of each type for each period
    """

    population_rate = [[rates[0], rates[1]]]

    for t in range(periods - 1):
        players = player.player_distribution(types, population_rate[-1], size_population)
        strategies = strategy.identity_assignment(players)
        matches = matching.random_matching(strategies)
        replications = replication.hawk_dove(matches)
        population = mutation.binary_uncorrelated(types, replications, size_population, mutation_rate)

        population_rate.append(population)

    return population_rate


def population_diagram(
        game='hawk_dove', types=[0, 1], rates=[0.4, 0.6], match='random', mutation_rate=0.1,
        size_population=100, periods=100
):
    population_rate = population_ratio(game, types, rates, match, mutation_rate, size_population, periods)
    diagrams.time_population_ratio(population_rate)
