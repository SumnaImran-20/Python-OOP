from abc import ABC, abstractmethod
#ABC = Abstract Base Classes
print("---Abstraction---")

class Polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass
    #non abstract method
    def color(self):
        print("Yellow color")

class Triangle(Polygon):
    def no_of_sides(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    def no_of_sides(self):
        print("I have 5 sides")

class Hexagon(Polygon):
    def no_of_sides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):
    def no_of_sides(self):
        print("I have 4 sides")
#Driver Code
T = Triangle()
T.no_of_sides()
T.color()

P = Pentagon()
P.no_of_sides()

H = Hexagon()
H.no_of_sides()

Q = Quadrilateral()
Q.no_of_sides()
