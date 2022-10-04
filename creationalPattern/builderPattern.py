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


class Builder:
    def getWheel(self):
        pass

    def getEngine(self):
        pass

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
