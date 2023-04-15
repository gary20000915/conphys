import math

from data import *
from model import *


class Bird(Character):
    def __init__(self, name: str) -> None:
        self.mass = 1.0
        super().__init__(name)

    def set_vel_and_angle(self, velocity: float, angle: float) -> None:
        ang_rad = math.radians(angle)
        vx = velocity * math.cos(ang_rad)
        vy = velocity * math.sin(ang_rad)
        self.point.vx = vx
        self.point.vy = vy

        return

    def apply_forc(self, fx: float, fy: float) -> None:
        m = self.mass
        self.point.ax = fx / m
        self.point.ay = fy / m

        return


class Pig(Character):
    def __init__(self, name: str, distance: float) -> None:
        self.distance = distance
        point = Point(t=0, x=distance, y=0, vx=0, vy=0, ax=0, ay=0)
        tra = Trajectory(
            lst_t=[], lst_x=[], lst_y=[], lst_vx=[], lst_vy=[], lst_ax=[], lst_ay=[]
        )
        super().__init__(name, point, tra)

        return

    def set_vel(self, speed: float) -> None:
        self.point.vx = speed
        return


class Game:
    def __init__(self, bird: Bird, pigs: list) -> None:
        self.bird = bird
        self.pigs = pigs

        return

    def run_pig(self, i: int, pigs: Pig) -> None:

        pigs = self.pigs[i]
        bird = self.bird
        TIME = bird.point.t
        time = 0
        pigs.point.t = time
        dt = 0.1
        while abs(TIME - time) > 0:
            time += dt
            pigs.update_to(new_time=time)

            if time > 2:
                print("Time out error!")
                break

        pigs.tra.dump(fn=f"Trajectory_pig{i}.txt")

        return print(f"Success to dump pig {i}!")

    def run_bird(self, bird: Bird) -> None:
        time = 0
        bird.point.t = time
        dt = 0.1
        while (
            bird.point.x >= 0
            and bird.point.x <= 100
            and bird.point.y >= 0
            and bird.point.y <= 50
        ):
            time += dt
            bird.update_to(new_time=time)

            if time > 30:
                print("Time out!")
                break

        bird.tra.dump(fn=f"Trajectory_bird.txt")
        bird.tra.plot_trajectory(show=False)

        print(f"Success to dump bird!")

        return

    def play(self):
        """
        The main function to play the angry bird game.
        """
        bird = self.bird
        pigs = self.pigs

        self.run_bird(bird)
        for i in range(len(pigs)):
            self.run_pig(i, pigs[i])
            d = bird.distance_to(pigs[i].point)
            tor = 2
            if abs(d - pigs[i].point.x) <= tor:
                print("Win")
            else:
                print(f"No! Pig{i} escape!")
        return


if __name__ == "__main__":
    bird = Bird(name="Angry Bird")
    bird.set_vel_and_angle(31.4, 45.0)
    bird.apply_forc(fx=0, fy=-9.81)

    pig1 = Pig("Pig1", distance=50.0)
    pig1.set_vel(speed=1.0)
    pig2 = Pig("Pig2", distance=100.0)
    pig2.set_vel(speed=-1.0)
    pig3 = Pig("Pig3", distance=10.0)
    pig3.set_vel(speed=2.0)
    pig_rest = Pig("Pig_rest", distance=100.0)
    pig_rest.set_vel(speed=0.0)

    # game = Game(bird, [pig1, pig2, pig3])
    game = Game(bird, [pig1, pig2, pig3, pig_rest])
    game.play()
