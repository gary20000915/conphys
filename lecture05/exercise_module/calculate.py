import numpy as np


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


if __name__ == "__main__":
    pos = np.array([0, 0])
    print(cla(pos, 31.4, 45, 4))
