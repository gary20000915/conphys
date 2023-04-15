import judge as j
import numpy as np

import output as o


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

        j.judge(pig, x0, y0, v0, theta)
        o.plot(True)


if __name__ == "__main__":
    Game()
