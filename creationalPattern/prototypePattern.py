"""Prototype pattern: runnable example.

A Prototype is an existing object that you copy to make new ones.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/prototype.md

Run it:  python prototypePattern.py
"""

from abc import ABC, abstractmethod
import copy


class Shape(ABC):
    @abstractmethod
    def getposition(self):
        pass

    @abstractmethod
    def clone(self):
        pass


class Square(Shape):
    def __init__(self, x=300, y=300):
        self.x, self.y = x, y
        self.tags = []                      # a mutable attribute, to show shallow versus deep copy

    def getposition(self):
        print('X:', self.x, 'Y:', self.y)

    def clone(self):
        return copy.deepcopy(self)          # independent copy, including nested objects


class Rectangle(Shape):
    def __init__(self, x=300, y=500):
        self.x, self.y = x, y
        self.tags = []

    def getposition(self):
        print('X:', self.x, 'Y:', self.y)

    def clone(self):
        return copy.deepcopy(self)


print('Square')
sqprototype = Square()
newsqprototype = sqprototype.clone()
print('Prototype is clone?', sqprototype is newsqprototype)      # False: a different object
newsqprototype.x = 10                                            # changing the clone ...
sqprototype.getposition()                                        # ... does not change the prototype
newsqprototype.getposition()

print('\nRectangle')
rectprototype = Rectangle()
newrectprototype = rectprototype.clone()                         # clone the RECTANGLE prototype
print('Same class as the prototype?', type(newrectprototype) is type(rectprototype))
newrectprototype.tags.append('copy')
print('Prototype tags:', rectprototype.tags, '| clone tags:', newrectprototype.tags)

# Shallow versus deep copy: copy.copy shares the nested list, deepcopy does not
shallow = copy.copy(rectprototype)
shallow.tags.append('shared')
print('After shallow copy, prototype tags:', rectprototype.tags)  # the prototype changed too!
