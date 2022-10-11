# imports to make abstract class and methods
from abc import abstractclassmethod, ABC

# making abstract Shape class or template for other shape classes
class Shape(ABC):
    @abstractclassmethod
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

# Creating Factory template to make factories 
class Factory(object):
    @abstractclassmethod
    def getShape(self):
        pass

# creating simple factory to make simple shapes
class SimpleFactory(Factory):
    def getShape(self, shape):
        return globals()[shape]()


# creating Round factory to make Rounded shapes
class RoundedFactory(Factory):
    def getShape(self, shape):
        shape = 'Rounded'+shape
        return globals()[shape]()

# Creating Main Abstract Factory to Create Factories which in turn create corresponding shapes
class AbstractFactory(object):
    def getFactory(self, rounded, shape):
        if rounded == True:
            return RoundedFactory().getShape(shape)
        else:
            return SimpleFactory().getShape(shape)


# Example

# creating a Abstract Factory
shape_factory = AbstractFactory()

# creating sub factories using Main Abstract Factory
shape_factory.getFactory(True, 'Circle').draw()
shape_factory.getFactory(True, 'Rectangle').draw()
shape_factory.getFactory(False, 'Circle').draw()
shape_factory.getFactory(False, 'Rectangle').draw()


# Theory:
#      Abstract Factory is Main Factory which have sub-factories that perform work.
# We put similar type of shapes in one factory like rounded shapes i.e.RoundedCircle,
# RoundedRectangle, are created by Rounded Factory and same goes for other simple shapes.
# Its hierarchy is below.

#                           Abstract Factory
#             Simple Factory              Rounded Factory
#         Circle       Rectangle     RoundedCircle   RoundedRectangle
