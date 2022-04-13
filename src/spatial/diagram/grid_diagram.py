import matplotlib.pyplot as plt
import seaborn as sns


def institution_grid(grid, institutions=[]):

    plt.figure()

    # players into the grid
    ax = sns.heatmap(grid, linewidths=.1)

    # institutions
    for border in institutions:
        ax.hlines(y=border[1][0], xmin=border[0][0], xmax=border[0][1], linestyle='--', linewidth=5, color="orange")
        ax.hlines(y=border[1][1], xmin=border[0][0], xmax=border[0][1], linestyle='--', linewidth=5, color="orange")
        ax.vlines(x=border[0][0], ymin=border[1][0], ymax=border[1][1], linestyle='--', linewidth=5, color="orange")
        ax.vlines(x=border[0][1], ymin=border[1][0], ymax=border[1][1], linestyle='--', linewidth=5, color="orange")

    # initialize color bar/ legend #TODO
    color_bar = ax.collections[0].colorbar
    color_bar.set_ticks([0, 1, 2])
    color_bar.set_ticklabels(['empty', 'type A', 'type B'])

    # no labels
    plt.axis('off')

    plt.show()
