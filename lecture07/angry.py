"""

This is a non-interactive version of the text-based angry bird game.

Usage: 

    python angry.py <velocity [m/s]> <angle [degree]>

Example:

    python angry.py 32.4 45


2023.03.26
Kuo-Chuan

"""
import math
from argparse import ArgumentParser
from typing import List

import matplotlib.pyplot as plt

# Constants
G = 9.81  # gravitational accerlation      [m/s/s]
DISTANCE = 100  # distance to the pig            [m]
DX = 1  # error tolerance                [m]
DT = 0.1  # time step to record trajectory [sec]

parser = ArgumentParser()
parser.add_argument("-v", "--velocity", type=float, default=20, help="Velocity.")
parser.add_argument("-a", "--angle", type=float, default=40, help="Angle.")
parser.add_argument(
    "-p",
    "--plot",
    dest="show_plot",
    action="store_true",
    default=False,
    help="Plot the figures.",
)
parser.add_argument(
    "-nl",
    "--nolog",
    dest="not_save_traj",
    action="store_false",
    default=True,
    help="Save the data.",
)
argv = parser.parse_args()


def play():
    """
    The main function to play the angry bird game.
    """

    try:
        velocity = argv.velocity  # 33.0 # m/s
        angle = argv.angle  # 45.0 # degree
    except:
        msg = """
        Error: incorrect inputs.

            Usage:

                python angry.py <velocity> <angle>

            Example: 

                python angry.py 32 45

        """
        print(msg)
        return

    print(f"The input velociy is {velocity}")
    print(f"The input angle is {angle}")
    values = [velocity, angle]
    distance = calculate_trajectory(values)

    if abs(distance - DISTANCE) <= DX:
        print("You win!!!")
    else:
        print(f"Ooopps. dx = {distance - DISTANCE}")

    return  # play()


def calculate_trajectory(values: List[float]) -> float:
    """
    Functio to calculate the trajectory of the angry bird

    :parama values: [velocity, angle]
    :return: the distance to travel
    """
    v0 = values[0]
    angle = values[1]
    angle_rad = math.radians(angle)

    # calculate the travel distance
    distance = v0**2 * math.sin(2 * angle_rad) / G

    # calculate times, positions_x,_y, vx, vy, ..
    time = 2.0 * v0 * math.sin(angle_rad) / G  # total fly time
    nsteps = math.ceil(time / DT) + 1

    times = []
    posx = []
    posy = []
    velx = []
    vely = []

    t = 0.0
    vx0 = v0 * math.cos(angle_rad)
    vy0 = v0 * math.sin(angle_rad)
    for n in range(nsteps):
        # calculate time
        if t > time:
            t = time
        times.append(t)

        # calculate position and velocity
        x = vx0 * t
        y = vy0 * t - 0.5 * G * t**2
        vx = vx0
        vy = vy0 - G * t
        posx.append(x)
        posy.append(y)
        velx.append(vx)
        vely.append(vy)

        t += DT

    plot_trajectory(posx, posy)
    output(times, posx, posy, velx, vely)

    return distance


def output(
    times: List[float],
    posx: List[float],
    posy: List[float],
    velx: List[float],
    vely: List[float],
    dump=argv.not_save_traj,
):
    """
    Write the trajectory to a file

    :param times: a list to store time info
    :param posx: a list to store x positions
    :param posy: a list to store y positions
    :param velx: a list to store vx
    :param vely: a list to store vy

    :return: None
    """
    if dump == True:
        f = open("trajectory.txt", mode="w")
        f.write(
            "# {:>12}  {:>12}  {:>12}  {:>12}  {:>12}\n".format(
                "time [s]", "x [m]", "y [m]", "vx [m/s]", "vy [ms]"
            )
        )

        for t, x, y, vx, vy in zip(times, posx, posy, velx, vely):
            line = f"  {t:>12.6e}  {x:>12.6e}  {y:>12.6e}  {vx:>12.6e}  {vy:>12.6e}\n"
            f.write(line)

        f.close()
    return


def plot_trajectory(x: List[float], y: List[float], show=argv.show_plot):
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
    play()
