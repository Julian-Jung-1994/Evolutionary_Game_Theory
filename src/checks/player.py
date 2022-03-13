def constant_binary_distribution_checks(types, rates, size_population):

    # rate checks
    rates_arr = np.array(rates)
    if not 0 <= rates_arr.any() <= 1:
        raise Exception('rates must be in range of [0, 1]')
    elif rates_arr.sum() != 1:
        raise Exception('population rates do not add up to 1')