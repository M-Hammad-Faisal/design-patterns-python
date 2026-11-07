"""Strategy pattern: runnable example.

A Strategy is an interchangeable way of doing one job.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/strategy.md

Run it:  python strategyPattern.py
"""

from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def cost(self, weight_kg): ...

class Standard(ShippingStrategy):
    def cost(self, weight_kg): return 5 + 1.0 * weight_kg

class Express(ShippingStrategy):
    def cost(self, weight_kg): return 15 + 2.5 * weight_kg

class Order:                                            # the context
    def __init__(self, weight_kg, strategy):
        self.weight_kg, self.strategy = weight_kg, strategy
    def shipping(self):
        return self.strategy.cost(self.weight_kg)

order = Order(2, Standard())
print(order.shipping())                                 # 7.0
order.strategy = Express()                              # swap behavior at runtime
print(order.shipping())                                 # 20.0

class Overnight(ShippingStrategy):                      # a new option: no existing code edited
    def cost(self, weight_kg): return 30 + 4 * weight_kg
print(Order(2, Overnight()).shipping())                 # 38

class PercentDiscount:
    def __init__(self, percent): self.percent = percent
    def apply(self, price): return price * (1 - self.percent / 100)

class FlatDiscount:
    def __init__(self, amount): self.amount = amount
    def apply(self, price): return max(0, price - self.amount)

def checkout(price, discount):
    return discount.apply(price)

print(checkout(100, PercentDiscount(20)), checkout(100, FlatDiscount(15)))   # 80.0 85
