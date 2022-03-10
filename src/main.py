from src.modules import replication, matching, player, strategy, diagrams


def population_ratio(game='hawk_dove', types=[0, 1], rates=[0.4, 0.6], size_population=100, periods=100):
    """
    as of now, two type hawk-dove game.

    Parameters
    ----------
    game : str
        future: name of predefined string, or replication matrix as input
    types : list
        player's types (as of now not used)
    rates : list of floats - two entries
        population rates as entries.
    size_population : int
        total size of population
    periods : int
        number of repetitions the game is played

    Returns
    -------
    population_rate : list of floats -
        the population ratio of each type for each period
    """

    population_rate = [[rates[0], rates[1]]]

    for t in range(periods - 1):
        players = player.constant_binary_distribution(population_rate[-1], size_population)
        strategies = strategy.identity_assignment(players)
        matches = matching.random_matching(strategies)
        replications = replication.hawk_dove(matches)

        population_rate.append(replications)

    return population_rate


def population_diagram(game='hawk_dove', types=[0, 1], rates=[0.4, 0.6], size_population=100, periods=100):

    population_rate = population_ratio(game, types, rates, size_population, periods)
    diagrams.time_population_ratio(population_rate)
