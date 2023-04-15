"""
This is the exercise for the Angry Birds. 

Author : Y. Gary Peng
Data   : March 13, 2023
Email  : garyphys0915@gapp.nthu.edu.tw
License: MIT
"""

import numpy as np

import output as out


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


def Game() -> None:
    """
    This is the main function of the game including I/O.
    """

    pig = np.array([100, 0])
    x0, y0 = 0, 0

    print("If wanting to quit the game, please type: quit")

    while True:
        try:
            """
            use 'space' to split two input data.
            """

            io = input("Input initial velocity (m/s) and initial angel (degree): \n")
            if io.lower() == "quit":
                print("Quit the game! \n")
                break
            # lst[velocity, angle]
            lst = io.split()
            v0, theta = float(lst[0]), float(lst[1])
            if len(lst) != 2:
                """
                Only let 2 inputs will go through this criteria.
                """

                raise Exception()
        except:
            print("Invalid inputs! \n")
            continue

        if v0 > 100:
            print("Velocity is too large! \n")
        if theta > 90 and theta < 0:
            print("Angel needs to be between 0 and 90! \n")

        print("Input correct! \n")

        judge(pig, x0, y0, v0, theta)
        out.plot(True)


def judge(pig: np.ndarray, x0: float, y0: float, v0: float, theta: float) -> None:
    """
    This is the judge function.

    :param pig: the position of the pig.
    :param x0: the initial position of the bird.
    :param y0: the initial position of the bird.
    :param v0: the initial velocity of the bird.
    :param theta: the initial angle of the bird.
    """

    t = 0
    dt = 0.1  # time step
    tor = 1  # pig radius + bird radius
    pos0 = np.array([x0, y0])

    # Write the output file
    f = open("trajectory.txt", mode="w", encoding="utf-8")
    f.write("# Header: trajectory of angry bird. \n\n")
    name = ["x [m]", "y [m]", "t [s]"]
    f.write(f"{name[0]:>6}  {name[1]:>6}  {name[2]:>6} \n")
    f.write(f"{pos0[0]:>6.3f}  {pos0[1]:>6.3f}  {0:>6.3f} \n")
    while True:
        # update timesteps
        t += dt

        # write the new position and the time in the output file
        pos = cla(pos0, v0, theta, t)
        f.write(f"{pos[0]:>6.3f}  {pos[1]:>6.3f}  {t:>6.3f} \n")

        # Judgement of results
        if d(pig, pos) < tor or d(pig, pos) == tor:
            print("Hit the PIG!")
            print(f"Comsuming time: {t:.3f} \n")
            break
        if pos[1] < pig[1] or pos[0] > pig[0]:
            print("Out of the filed! Distance:", f"{d(pig, pos):.3f}")
            print(
                "bird - pig = [dx, dy]:",
                f"[{(pos - pig)[0]:.3f}, {(pos - pig)[1]:.3f}] \n",
            )
            break
        if t > 1000:
            print("Take too much time!")
            print("Not hit the PIG! Distance:", f"{d(pig, pos):.3f} \n")
            break


if __name__ == "__main__":
    Game()
    # ans: v0, theta = 33.5, 60
    # ans: v0, theta = 31.4, 45
