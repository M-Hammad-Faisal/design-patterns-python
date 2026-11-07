"""Factory Method pattern: runnable example.

A factory creates objects for you, so callers ask by name instead of naming concrete classes.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/factory-method.md

Run it:  python factoryPattern.py
"""

from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def getColor(self):
        pass


class Red(Color):
    def getColor(self):
        print('I am Red')


class Blue(Color):
    def getColor(self):
        print('I am Blue')


class Green(Color):
    def getColor(self):
        print('I am Green')


class ColorFactory:
    # An explicit dictionary of allowed classes is safer than globals()[name]():
    # unknown names give a clear error instead of reaching arbitrary objects.
    colors = {'Red': Red, 'Green': Green, 'Blue': Blue}

    def createColor(self, color):
        color = color.capitalize()
        try:
            return self.colors[color]()
        except KeyError:
            raise ValueError(
                f"unknown color {color!r}; choose from {sorted(self.colors)}") from None


# Example
color_factory = ColorFactory()
color = ['red', 'green', 'blue']

for c in color:
    color_factory.createColor(c).getColor()

try:
    color_factory.createColor('purple')
except ValueError as error:
    print(error)


# ---------------------------------------------------------------------------
# Self-registering factory: new colors register themselves, the factory
# code never has to change (Open/Closed Principle).
class AutoColor:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        AutoColor.registry[cls.__name__.lower()] = cls

    @classmethod
    def create(cls, name):
        return cls.registry[name]()

    def getColor(self):
        print(f'I am {type(self).__name__}')


class Yellow(AutoColor):
    pass


class Purple(AutoColor):
    pass


AutoColor.create('yellow').getColor()
AutoColor.create('purple').getColor()
