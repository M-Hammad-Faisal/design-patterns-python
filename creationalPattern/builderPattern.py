"""Builder pattern: runnable example.

A Builder constructs a complex object step by step and hands it over when it is finished.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/builder.md

Run it:  python builderPattern.py
"""

from abc import ABC, abstractmethod


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print("Body: %s" % self.__body.shape)
        print("Engine horsepower: %d" % self.__engine.horsepower)
        print("Tire size: %d\'" % self.__wheels[0].size)


class Builder(ABC):
    @abstractmethod
    def getWheel(self):
        pass

    @abstractmethod
    def getEngine(self):
        pass

    @abstractmethod
    def getBody(self):
        pass


class JeepBuilder(Builder):

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "My Car"
        return body
    
class TruckBuilder(Builder):

    def getWheel(self):
        wheel = Wheel()
        wheel.size = 28
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 1200
        return engine

    def getBody(self):
        body = Body()
        body.shape = "My Truck"
        return body


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setBody(body)

        engine = self.__builder.getEngine()
        car.setEngine(engine)

        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1
        return car


jeepBuilder = JeepBuilder()
truckBuilder = TruckBuilder()
director = Director()

print("Jeep")
director.setBuilder(jeepBuilder)
jeep = director.getCar()
jeep.specification()
print()
print("Truck")
director.setBuilder(truckBuilder)
truck = director.getCar()
truck.specification()


# ---------------------------------------------------------------------------
# Fluent builder: the Pythonic, chainable style (each step returns self).
# Validation happens once, in build().
class CarSpec:
    def __init__(self, body, engine_hp, wheel_size, wheels):
        self.body, self.engine_hp, self.wheel_size, self.wheels = body, engine_hp, wheel_size, wheels

    def __repr__(self):
        return f"CarSpec({self.body!r}, {self.engine_hp}hp, {self.wheels} wheels of {self.wheel_size}')"


class CarBuilder:
    def __init__(self):
        self._body, self._hp, self._size, self._wheels = None, 150, 17, 4

    def body(self, shape):
        self._body = shape
        return self

    def engine(self, horsepower):
        self._hp = horsepower
        return self

    def wheels(self, count, size):
        self._wheels, self._size = count, size
        return self

    def build(self):
        if self._body is None:
            raise ValueError("a car needs a body")
        return CarSpec(self._body, self._hp, self._size, self._wheels)


print()
print(CarBuilder().body("Hatchback").engine(120).build())
print(CarBuilder().body("Monster truck").engine(900).wheels(4, 40).build())
try:
    CarBuilder().build()
except ValueError as error:
    print("Rejected:", error)
