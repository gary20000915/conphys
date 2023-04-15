"""

A python class that can do arbitray finite integral of a funcn from a to b
Note that we don't consider the performance in this example.

To use it, you need to define a function first

import math

def my_func(x):
    return math.sqrt(x)  

integrate = Integrator(func)    
area =  integrate.midpoint(a=0,b=2,N=1000)

"""
import math


class Integrator:
    def __init__(self, func):
        """
        setup the integrator with a given function
        """
        self.f = func
        return

    def midpoint(self, a=-1, b=1, N=int(10_000)):
        """
        Assume a < b
        """
        f = self.f
        dx = (b - a) / int(N)
        area = 0
        for n in range(int(N)):
            xn = a + (0.5 + n) * dx
            area += dx * f(xn)
        return area

    def trap(self, a=-1, b=1, N=int(10_000)):
        """
        Assume a < b
        """
        f = self.f
        dx = (b - a) / int(N)
        area = 0
        for n in range(int(N)):
            xn = a + n * dx
            u = f(xn + dx)
            l = f(xn)
            area += (u + l) * dx * 0.5
        return area

    def trapz(self, a=-1, b=1, N=int(10_000)):
        """
        Assume a < b
        """
        f = self.f
        dx = (b - a) / int(N)
        area = 0
        for n in range(int(N)):
            xn = a + n * dx
            u = f(xn + dx)
            l = f(xn)
            area += (u + l) * dx * 0.5
        return area

    def simp(self, a=-1, b=1, N=int(10_000)):
        """
        Assume a < b
        """
        f = self.f
        dx = (b - a) / int(N)
        area = 0
        for n in range(int(N)):
            l = f(a + (n + 1) * dx)
            m = f(a + (n + 0.5) * dx)
            r = f(a + n * dx)
            area += dx / 6 * (r + 4 * m + l)
        return area


if __name__ == "__main__":

    def hcirc(x):
        return math.sqrt(1 - x**2)

    integrate = Integrator(func=hcirc)
    area = integrate.simp(a=-1, b=1, N=1e5)
    print(2 * area)
