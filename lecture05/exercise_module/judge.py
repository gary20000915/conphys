import calculate as c
import distance as d
import numpy as np


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
        pos = c.cla(pos0, v0, theta, t)
        f.write(f"{pos[0]:>6.3f}  {pos[1]:>6.3f}  {t:>6.3f} \n")

        # Judgement of results
        if d.d(pig, pos) < tor or d.d(pig, pos) == tor:
            print("Hit the PIG!")
            print(f"Comsuming time: {t:.3f} \n")
            break
        if pos[1] < pig[1] or pos[0] > pig[0]:
            print("Out of the filed! Distance:", f"{d.d(pig, pos):.3f}")
            print(
                "bird - pig = [dx, dy]:",
                f"[{(pos - pig)[0]:.3f}, {(pos - pig)[1]:.3f}] \n",
            )
            break
        if t > 1000:
            print("Take too much time!")
            print("Not hit the PIG! Distance:", f"{d.d(pig, pos):.3f} \n")
            break


if __name__ == "__main__":
    judge(np.array([0, 100]), 0, 0, 31.4, 45)
