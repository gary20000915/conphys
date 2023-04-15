"""

This script is used as a demo to visualize your angry bird trajectories.

Reuirement: matplotlib.

If you haven't install matplotlib, enter your `comphys` envrioment and then type

    conda install matplotlib

"""
import matplotlib.pyplot as plt


def plot_trajectory(x, y, show=True):
    """
    Plot the trajectroy and save it as a png file.

    :param x: a python list that inlcudes the x positions of a trajectory
    :param y: a python list that includes the y positions of a trajectory
    :param show: show the plot or not

    both lists must have the same length
    """
    if len(x) != len(y):
        print("Error: the length of the lists x and y must be the same!")
    else:
        plt.figure(1, figsize=(8, 6))
        plt.plot(x, y, "-o")
        plt.xlabel(" X [code units]")
        plt.ylabel(" Y [code units]")
        plt.savefig("fig_trajectory.png")
        if show:
            plt.show()
    return


if __name__ == "__main__":

    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plot_trajectory(x, y, show=True)
