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


class ColorFactory():
    def createColor(self, color):
        color = color.capitalize()
        return globals()[color]()

# Example
color_factory = ColorFactory()
color = ['red', 'green', 'blue']

for c in color:
    color_factory.createColor(c).getColor()
