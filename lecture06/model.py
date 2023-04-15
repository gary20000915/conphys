import math

from data import Point, Trajectory


class Character:
    def __init__(self, name: str, point=Point(), tra=Trajectory()) -> None:
        self.name = name
        self.point = point  # old point
        self.tra = tra

    def update_to(self, new_time: float) -> None:
        t0 = self.point.t
        vx0 = self.point.vx
        vy0 = self.point.vy
        x0 = self.point.x
        y0 = self.point.y
        ax0 = self.point.ax
        ay0 = self.point.ay

        x = x0 + vx0 * (new_time - t0)
        y = y0 + vy0 * (new_time - t0) - 0.5 * ay0 * (new_time - t0) ** 2
        vx = vx0 + 0.5 * ax0 * (new_time - t0) ** 2
        # print("vx:", vx)
        vy = vy0 + self.point.ay * (new_time - t0)
        # print("vy:", vy)
        ax = ax0
        ay = ay0
        # print("ay:", ay)

        self.point.x = x
        self.point.y = y
        self.point.vx = vx
        self.point.vy = vy
        self.point.ax = ax
        self.point.ay = ay
        self.point.t = new_time

        self.tra.append(self.point)

        return

    def distance_to(self, point: Point) -> float:
        p1 = self.point  # new point
        p2 = point

        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


if __name__ == "__main__":
    bird = Character(name="Angry Bird")
    bird.point.vx = 0.5
    print(bird.point)
    print(bird.tra)
    print(bird.name)

    pig = Point()
    pig.x = 100

    dt = 0.1
    time = 0

    for i in range(10):
        time += dt
        bird.update_to(new_time=time)
        # print(bird.point.x, bird.point.y, bird.point.t)

    d = bird.distance_to(pig)
    tor = 0.1
    if abs(d - pig.x) <= tor:
        print("Win")
    print(d)
