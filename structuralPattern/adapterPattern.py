"""Adapter pattern: runnable example.

An Adapter translates one interface into another so incompatible classes can work together.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/adapter.md

Run it:  python adapterPattern.py
"""

class US:
    """The interface our application expects: speed in kilometers."""
    def __init__(self, speed):
        self.__speed = speed

    def getSpeed(self):
        return str(self.__speed) + ' Kilometers'


class UK:
    """A class we cannot change (think: a third-party library): it reports MILES."""
    def __init__(self, speed):
        self.__speed = speed

    def getSpeedM(self):
        return self.__speed


class Adapter:
    """Wraps a UK object and offers the US interface (getSpeed in kilometers)."""
    MILES_TO_KM = 1.60934

    def __init__(self, uk):
        self.__uk = uk                       # composition: hold the object we adapt

    def getSpeed(self):
        kilometers = self.__uk.getSpeedM() * self.MILES_TO_KM
        return f"{kilometers:.1f} Kilometers"


# The client only knows ONE interface: getSpeed()
def show_speed(label, vehicle):
    print(f"{label}: {vehicle.getSpeed()}")


speed = 100

# Already in kilometers: works directly
show_speed("Speed in US", US(speed))

# UK reports miles, so it has no getSpeed(). We do not touch UK: we wrap it.
show_speed("Speed in UK (adapted)", Adapter(UK(speed)))
