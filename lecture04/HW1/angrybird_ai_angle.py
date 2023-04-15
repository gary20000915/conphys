"""
This is the homework for the Angry Birds with bisection method utilizing definite velocity v0.
Try to use bisection method to find out the angle theta.

Author : Y. Gary Peng
Data   : March 13, 2023
Email  : garyphys0915@gapp.nthu.edu.tw
License: MIT
"""

import string

import numpy as np

import output as o


def cla(pos0: np.ndarray, v0: float, theta: float, t: float) -> np.ndarray:
    """
    This is the function to calculate the position of the bird.

    :param pos0: the initial position of the bird.
    :param v0: the initial velocity of the bird.
    :param theta: the initial angle of the bird.
    :param t: the current time.
    """

    g = -9.81  # m/s^2
    x = pos0[0] + v0 * np.cos(np.pi * theta / 180) * t
    y = pos0[1] + v0 * np.sin(np.pi * theta / 180) * t + 0.5 * g * np.square(t)
    return np.array([x, y])


def d(pig: np.ndarray, pos: np.ndarray) -> float:
    """
    This is the function to calculate the distance between the bird and pig.

    :param pig: the position of the pig.
    :param pos: the position of the bird.
    """

    return np.sqrt(np.sum(np.square(pos - pig)))


def Game(path) -> None:
    """
    This is the main function of the game including I/O.

    :param path: path of the file name.
    """

    pig = np.array([100, 0])
    x0, y0 = 0, 0

    print("If wanting to quit the game, please type: quit")
    print("(One possible answer is [40, 50])")

    while True:
        try:
            """
            use "space" to split two input data.
            """

            io = input("Input bisection interval a, b: \n")
            if io.lower() == "quit":
                print("Quit the game! \n")
                break
            lst = io.split()
            a, b = float(lst[0]), float(lst[1])
            if len(lst) != 2:
                """
                Only let 2 input go through this criteria.
                """
                raise Exception()
        except:
            print("Invalid inputs! \n")
            continue  # jump to the next index.

        print("Input correct! \n")
        print("... please wait ... \n")

        judge(path, pig, x0, y0, a, b)
        o.plot(path, show=False)


def bi(a, b, pos0, t, v0) -> tuple:
    i = 0
    x = 0  # default value
    err = 1e-3
    while 0.5 * (b - a) > err:
        x = 0.5 * (a + b)
        i += 1
        pos = cla(pos0, v0, x, t)
        pos_temp = cla(pos0, v0, a, t)
        if pos[1] * pos_temp[1] < 0:
            b = x
        else:
            a = x
        if i > 1e3:
            print(f"angle = {x:3f} and t = {t:3f}")
            print("Too long!")
            break
    return x, i


def judge(path: str, pig: np.ndarray, x0: float, y0: float, a: float, b: float) -> None:
    """
    This is the judge function and we consider the judge function as bird's height.
    Note that [a, b] needs to include the solution of y = 0.
    Here we use the initial velocity v0 = 31.5.

    :param path: path of the file name.
    :param pig: the position of the pig.
    :param x0 : the initial position of the bird.
    :param y0 : the initial position of the bird.
    :param a  : the start interval of bisection method.
    :param b  : the end interval of bisection method.
    """

    t = 0
    dt = 1e-4  # time step
    tor = 1e-2  # pig radius + bird radius
    pos0 = np.array([x0, y0])
    v0 = 31.5  # the initial velocity

    # Write the output file
    f = open(path + ".txt", mode="w", encoding="utf-8")
    f.write("# Header: trajectory of angry bird. \n\n")
    name = ["x [m]", "y [m]", "t [s]"]
    f.write(f"{name[0]:>6}  {name[1]:>6}  {name[2]:>6} \n")
    f.write(f"{pos0[0]:>6.3f}  {pos0[1]:>6.3f}  {0:>6.3f} \n")
    while True:
        theta, i = bi(a, b, pos0, t, v0)[0], bi(a, b, pos0, t, v0)[1]
        pos = cla(pos0, v0, theta, t)
        f.write(f"{pos[0]:>6.3f}  {pos[1]:>6.3f}  {t:>6.3f} \n")
        if d(pig, pos) < tor or d(pig, pos) == tor:
            print("Hit the PIG!")
            print("Initial angle:", f"{theta:.3f}")
            print(f"Used {i} trails.")
            print(f"Comsuming time: {t:.3f} \n")
            break

        if t > 10:
            print("Take too much time!")
            print("Not hit the PIG! Distance:", f"{d(pig, pos):.3f}")
            print(f"The recent used angle is: {theta:.3f}")
            print("Initial velocity:", f"{v0:.3f}")
            print(f"Used {i} trails.")
            print(f"Comsuming time: {t:.3f} \n")
            break
        t += dt


if __name__ == "__main__":
    path = "trajectory_bisection_angle"
    Game(path)
    # ans: [a, b] = [40, 50]
