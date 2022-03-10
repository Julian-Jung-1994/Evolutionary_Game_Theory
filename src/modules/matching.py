import random


def random_matching(strategies):

    # utilize random.shuffle function: randomly changes items of list
    player_shuffle = strategies.copy()
    random.shuffle(player_shuffle)

    # split players into two halves and then match the n-th entries of both splits
    first_half = player_shuffle[:int(len(player_shuffle)/2)]
    second_half = player_shuffle[int(len(player_shuffle)/2):]
    matches = list(zip(first_half, second_half))

    return matches
