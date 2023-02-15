# class Circle:

#     def __init__(self, diameter):
#         self.diameter = diameter

#     def area(self, pi=3.14):
#         return pi*(self.diameter/2)**2

#     def bigger(self, other_circle)

# circle1 = Circle(100)
# print(circle1.area())


import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified")

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius:.2f}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

circles = [Circle(radius=3), Circle(diameter=4), Circle(radius=1)]
print(sorted(circles))
