from dataclasses import dataclass, field
from typing import List

from matplotlib import pyplot as plt


@dataclass
class Point:
    t: float = 0.0
    x: float = 0.0
    y: float = 0.0
    vx: float = 0.0
    vy: float = 0.0
    ax: float = 0.0
    ay: float = 0.0


@dataclass
class Trajectory:
    lst_t: List[float] = field(default_factory=lambda: [])
    lst_x: List[float] = field(default_factory=lambda: [])
    lst_y: List[float] = field(default_factory=lambda: [])
    lst_vx: List[float] = field(default_factory=lambda: [])
    lst_vy: List[float] = field(default_factory=lambda: [])
    lst_ax: List[float] = field(default_factory=lambda: [])
    lst_ay: List[float] = field(default_factory=lambda: [])

    def append(self, point: Point) -> None:
        self.lst_t.append(point.t)
        self.lst_x.append(point.x)
        self.lst_y.append(point.y)
        self.lst_vx.append(point.vx)
        self.lst_vy.append(point.vy)
        self.lst_ax.append(point.ax)
        self.lst_ay.append(point.ay)
        return

    def dump(self, fn="trajectory.txt") -> None:
        f = open(fn, mode="w")
        f.write(
            "# {:>12}  {:>12}  {:>12}  {:>12}  {:>12}  {:>12}  {:>12}\n".format(
                "time [s]",
                "x [m]",
                "y [m]",
                "vx [m/s]",
                "vy [ms]",
                "ax [m/s*s]",
                "ay [m/s*s]",
            )
        )

        for t, x, y, vx, vy, ax, ay in zip(
            self.lst_t,
            self.lst_x,
            self.lst_y,
            self.lst_vx,
            self.lst_vy,
            self.lst_ax,
            self.lst_ay,
        ):
            line = f"  {t:>12.6e}  {x:>12.6e}  {y:>12.6e}  {vx:>12.6e}  {vy:>12.6e}  {ax:>12.6e}  {ay:>12.6e}\n"
            f.write(line)

        f.close()

    def plot_trajectory(self, show=False):
        """
        Plot the trajectroy and save it as a png file.

        :param x: a python list that inlcudes the x positions of a trajectory
        :param y: a python list that includes the y positions of a trajectory
        :param show: show the plot or not

        both lists must have the same length
        """
        if len(self.lst_x) != len(self.lst_y):
            print("Error: the length of the lists x and y must be the same!")
        else:
            plt.figure(1, figsize=(8, 6))
            plt.plot(self.lst_x, self.lst_y, "-o")
            plt.xlabel(" X [code units]")
            plt.ylabel(" Y [code units]")
            plt.savefig("fig_trajectory.png")
            if show:
                plt.show()
        return


if __name__ == "__main__":
    p = Point(
        10,
        0,
        0,
        0,
        0,
        10,
        10,
    )
    print(p.t)
    tra = Trajectory()
    print(tra, tra.lst_x)
    tra.append(p)
    tra.dump()
