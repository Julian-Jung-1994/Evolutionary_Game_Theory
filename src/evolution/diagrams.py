import numpy as np
import matplotlib.pyplot as plt


def time_population_ratio(population_rate):  # TODO work with axes object

    population_rate = np.array(population_rate)

    plt.figure()

    plt.plot(np.arange(population_rate.shape[0]), population_rate[:, 0], label='Dove')
    plt.scatter(np.arange(population_rate.shape[0]), population_rate[:, 0])
    plt.plot(np.arange(population_rate.shape[0]), population_rate[:, 1], label='Hawk')
    plt.scatter(np.arange(population_rate.shape[0]), population_rate[:, 1])

    plt.title('Hawk Dove game')
    plt.legend()
    plt.xlabel('period')
    plt.ylabel('share of population')
    plt.ylim(0, 1)

    plt.show()
