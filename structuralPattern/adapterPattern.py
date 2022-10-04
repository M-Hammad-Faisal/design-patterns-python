class US:
    __speed = None

    def __init__(self, speed):
        self.__speed = speed

    def getSpeed(self):
        return str(self.__speed) + ' Kilometers'


class UK:
    __speed = None

    def __init__(self, speed):
        self.__speed = speed

    def getSpeedM(self, speed=None):
        if speed:
            return speed
        return str(self.__speed) + ' Kilometers'


class Adapter(US, UK):
    __speed = None

    def __init__(self, speed):
        self.__speed = speed

    def getSpeed(self):
        return str(self.getSpeedM(self.__speed) * 1.6) + ' Miles'


speed = 400

# Kilometers
usSpeed = US(speed)
print("Speed in US:", usSpeed.getSpeed())

# returns Kilometers but we want in Miles.
# we use Adapter
# ukSpeed = UK(speed)
# print("Speed in UK:", ukSpeed.getSpeedM())

# convert Kilometers to Miles
adapter = Adapter(speed)
print("Speed in UK:", adapter.getSpeed())
