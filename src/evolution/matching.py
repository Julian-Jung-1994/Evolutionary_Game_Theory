import random


def random_matching(strategies):

    # utilize random.shuffle function: randomly changes items of list
    strategies_shuffle = strategies.copy()
    random.shuffle(strategies_shuffle)

    # split players into two halves and then match the n-th entries of both splits
    first_half = strategies_shuffle[:int(len(strategies_shuffle)/2)]
    second_half = strategies_shuffle[int(len(strategies_shuffle)/2):]
    matches = list(zip(first_half, second_half))

    return matches
