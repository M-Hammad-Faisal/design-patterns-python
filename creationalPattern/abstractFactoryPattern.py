from abc import abstractmethod


class Shape(object):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('I am Circle.')


class Rectangle(Shape):
    def draw(self):
        print('I am Rectangle.')


class RoundedCircle(Shape):
    def draw(self):
        print('I am Rounded Circle.')


class RoundedRectangle(Shape):
    def draw(self):
        print('I am Rounded Rectangle.')


class Factory(object):
    @abstractmethod
    def getShape(self):
        pass


class SimpleFactory(Factory):
    def getShape(self, shape):
        return globals()[shape]()


class RoundedFactory(Factory):
    def getShape(self, shape):
        shape = 'Rounded'+shape
        return globals()[shape]()


class AbstractFactory(object):
    def getFactory(self, rounded, shape):
        if rounded == True:
            return RoundedFactory().getShape(shape)
        else:
            return SimpleFactory().getShape(shape)


# Example
shape_factory = AbstractFactory()
shape_factory.getFactory(True, 'Circle').draw()
shape_factory.getFactory(True, 'Rectangle').draw()
shape_factory.getFactory(False, 'Circle').draw()
shape_factory.getFactory(False, 'Rectangle').draw()
