import numpy as np
import matplotlib.pyplot as plt


def time_population_ratio(population_rate):  # TODO work with axes object

    population_rate = np.array(population_rate)

    plt.figure()

    plt.plot(np.arange(population_rate.shape[0]), population_rate[:, 0])
    plt.scatter(np.arange(population_rate.shape[0]), population_rate[:, 0])
    plt.plot(np.arange(population_rate.shape[0]), population_rate[:, 1])
    plt.scatter(np.arange(population_rate.shape[0]), population_rate[:, 1])

    plt.title('Hawk Dove game')
    plt.xlabel('period')
    plt.ylabel('population ratio')
    plt.ylim(0, 1)
    plt.yticks(np.arange(0, 1.2, 0.2), ['Dove', 0.2, 0.4, 0.6, 0.8, 'Hawk'])

    plt.show()
