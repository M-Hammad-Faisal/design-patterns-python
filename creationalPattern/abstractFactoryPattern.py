"""Abstract Factory pattern: runnable example.

An Abstract Factory creates whole families of related objects without naming their concrete classes.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/abstract-factory.md

Run it:  python abstractFactoryPattern.py
"""

# imports to make abstract class and methods
from abc import ABC, abstractmethod


# making abstract Shape class or template for other shape classes
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


#  Circle Shape
class Circle(Shape):
    def draw(self):
        print('I am Circle.')


#  Rectangle Shape
class Rectangle(Shape):
    def draw(self):
        print('I am Rectangle.')


# Rounded Circle Shape
class RoundedCircle(Shape):
    def draw(self):
        print('I am Rounded Circle.')


# Rounded Rectangle Shape
class RoundedRectangle(Shape):
    def draw(self):
        print('I am Rounded Rectangle.')


# Factory template to make factories (now really abstract: it cannot be created)
class Factory(ABC):
    @abstractmethod
    def getShape(self, shape):
        pass


# creating simple factory to make simple shapes
class SimpleFactory(Factory):
    shapes = {'Circle': Circle, 'Rectangle': Rectangle}

    def getShape(self, shape):
        return self.shapes[shape]()


# creating Round factory to make Rounded shapes
class RoundedFactory(Factory):
    shapes = {'Circle': RoundedCircle, 'Rectangle': RoundedRectangle}

    def getShape(self, shape):
        return self.shapes[shape]()


# Main Abstract Factory: chooses the right factory (family) for you
class AbstractFactory:
    def getFactory(self, rounded, shape):
        if rounded:
            return RoundedFactory().getShape(shape)
        return SimpleFactory().getShape(shape)


# Example

# creating a Abstract Factory
shape_factory = AbstractFactory()

# creating shapes using the Abstract Factory
shape_factory.getFactory(True, 'Circle').draw()
shape_factory.getFactory(True, 'Rectangle').draw()
shape_factory.getFactory(False, 'Circle').draw()
shape_factory.getFactory(False, 'Rectangle').draw()

# The abstract base class really protects us now:
try:
    Factory()
except TypeError as error:
    print("Cannot create the abstract Factory:", error)


# Theory:
#      Abstract Factory is Main Factory which have sub-factories that perform work.
# We put similar type of shapes in one factory like rounded shapes i.e.RoundedCircle,
# RoundedRectangle, are created by Rounded Factory and same goes for other simple shapes.
# Its hierarchy is below.

#                           Abstract Factory
#             Simple Factory              Rounded Factory
#         Circle       Rectangle     RoundedCircle   RoundedRectangle
