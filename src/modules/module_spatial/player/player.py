# TODO rounding problems with rate
def player_distribution(types=[1, 2], rates=[0.5, 0.5], size_population=10):

    players = []
    for rate in enumerate(rates):

        quote = rate[1] * size_population
        quote = int(quote)

        player_type = [types[rate[0]]]

        tmp = player_type * quote
        players.extend(tmp)

    return players
