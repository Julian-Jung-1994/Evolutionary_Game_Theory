from src.modules import replication, matching, player, strategy, diagrams


class Game:
    def __init__(self, types, rates, size_population, periods):
        """
        as of now, two type hawk-dove game.

        Parameters
        ----------
        types : list
            player's types (as of now not used)
        rates : list of floats - two entries
            population rates as entries.
        size_population : int
            total size of population
        periods : int
            number of repetitions the game is played
        """
        self.types = types
        self.rates = rates
        self.size_population = size_population
        self.periods = periods
        self.population = []

    def population_ratio(self):
        """
        Returns
        -------
        population_ratio : list of floats -
            the population ratio of each type for each period
        """
        # dictionary of types as key with list as population ratios
        population_ratio = [[self.rates[0], self.rates[1]]]

        for t in range(self.periods - 1):
            players = player.constant_binary_distribution(self.rates, self.size_population)
            strategies = strategy.identity_assignment(players)
            matches = matching.random_matching(strategies)
            replications = replication.hawk_dove(matches)

            population_ratio.append(replications)

        self.population.append(population_ratio)
        return population_ratio

    def diagram(self):

        population_rate = population_ratio()
        diagrams.time_population_ratio(population_rate)

# ([0,1], [0.4, 0.6], 100, 50)
