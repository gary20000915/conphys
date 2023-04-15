import visual as v


def plot(path: str, show=False):
    x, y, t = [], [], []
    f = open(path + ".txt", "r")
    for line in f.readlines():
        data = line.split("  ")
        try:
            x.append(float(data[0]))
            y.append(float(data[1]))
            t.append(float(data[2]))
        except:
            pass
    v.plot_trajectory(path, x, y, show)
    return


if __name__ == "__main__":
    plot("trajectory_bisection_angle", show=True)
