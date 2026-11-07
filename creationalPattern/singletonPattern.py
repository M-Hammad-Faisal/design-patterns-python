"""Singleton pattern: runnable example.

A Singleton guarantees that a class has exactly one instance.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/singleton.md

Run it:  python singletonPattern.py
"""


class Singleton:
    __instance = None

    def __str__(self):
        return "I am instance."

    def __init__(self):
        # Creating a second object directly is not allowed
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        Singleton.__instance = self

    @staticmethod
    def getinstance():
        # Static method: it has no "self", so it is called as Singleton.getinstance()
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


# Example
singleton = Singleton()
print(singleton)

same = Singleton.getinstance()
print("getinstance() returns the same object:", same is singleton)

try:
    Singleton()                                  # a second instance is refused
except Exception as error:
    print("Second instance rejected:", error)


# ---------------------------------------------------------------------------
# Pythonic version: control creation with __new__ (always the same object),
# thread-safe. A module-level object is often even simpler: see the lesson.
import threading


class Config:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.values = {}    # initialized once, not on every Config() call
        return cls._instance


a, b = Config(), Config()
a.values["mode"] = "prod"
print("Config():", a is b, b.values)
