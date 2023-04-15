import visual as v


def plot(show=False):
    x, y, t = [], [], []
    f = open("trajectory.txt", "r")
    for line in f.readlines():
        data = line.split("  ")
        try:
            x.append(float(data[0]))
            y.append(float(data[1]))
            t.append(float(data[2]))
        except:
            pass
    v.plot_trajectory(x, y, show)
    return


if __name__ == "__main__":
    plot()
