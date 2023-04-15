import numpy as np


def d(pig: np.ndarray, pos: np.ndarray) -> float:
    """
    This is the function to calculate the distance between the bird and pig.

    :param pig: the position of the pig.
    :param pos: the position of the bird.
    """

    return np.sqrt(np.sum(np.square(pos - pig)))


if __name__ == "__main__":
    pos = np.array([0, 0])
    pig = np.array([100, 0])
    print(d(pig, pos))
