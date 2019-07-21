class Dog:

    def __init__(self, breed):
        self.breed = breed


myDog = Dog(breed="Lab")
print(myDog.breed)


class Circle:
    pi = 3.14

    def __init__(self, radius= 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, radius):
        self.radius = radius


myC = Circle(3)
myC.set_radius(100)
print(myC.area())
