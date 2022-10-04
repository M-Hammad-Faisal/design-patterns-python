class Singleton:
    __instance = None

    def __str__(self):
        return "I am instance."

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def getinstance(self):
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance


singleton = Singleton()
print(singleton)
