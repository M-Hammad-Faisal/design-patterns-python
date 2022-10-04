from abc import abstractclassmethod, ABC
import copy


class Shape(ABC):
    x, y = None, None

    @abstractclassmethod
    def getposition(self):
        pass

    @abstractclassmethod
    def clone(self):
        pass


class Square(Shape):
    x, y = 300, 300

    def getposition(self):
        print('X:', self.x, 'Y:', self.y)

    def clone(self):
        return copy.copy(self)


class Rectangle(Shape):
    x, y = 300, 500

    def getposition(self):
        print('X:', self.x, 'Y:', self.y)

    def clone(self):
        return copy.copy(self)


print('Square')
sqprototype = Square()
newsqprototype = sqprototype.clone()
print('Prototype:', sqprototype)
print('Clone prototype:', newsqprototype)

print('\nRectangle')
rectprototype = Rectangle()
newrectprototype = sqprototype.clone()
print('Prototype:', rectprototype)
print('Clone prototype:', newrectprototype)
