"""State pattern: runnable example.

With State, an object changes how it behaves depending on what state it is in, and each state is its own small object that knows what to do and what state comes next.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/state.md

Run it:  python statePattern.py
"""

class Order:                                            # the context
    def __init__(self):
        self.state = Pending()
    def pay(self):    self.state = self.state.pay(self)
    def ship(self):   self.state = self.state.ship(self)
    def cancel(self): self.state = self.state.cancel(self)

class State:                                            # default behavior: not allowed
    name = "?"
    def pay(self, order):    raise ValueError(f"cannot pay in state {self.name}")
    def ship(self, order):   raise ValueError(f"cannot ship in state {self.name}")
    def cancel(self, order): raise ValueError(f"cannot cancel in state {self.name}")

class Pending(State):
    name = "pending"
    def pay(self, order):    return Paid()
    def cancel(self, order): return Cancelled()

class Paid(State):
    name = "paid"
    def ship(self, order):   return Shipped()
    def cancel(self, order): return Cancelled()

class Shipped(State):
    name = "shipped"                                    # no actions allowed any more

class Cancelled(State):
    name = "cancelled"

order = Order()
order.pay(); order.ship()
print(order.state.name)                                 # shipped
try:
    order.cancel()
except ValueError as e:
    print(e)                                            # cannot cancel in state shipped

try:
    Order().ship()                                      # cannot ship before paying
except ValueError as e:
    print(e)                                            # cannot ship in state pending

class Player:
    def __init__(self):
        self.state = Stopped()
    def press_play(self):                                # ONE button, behavior depends on the state
        self.state = self.state.press_play()
        return self.state.name

class Stopped:
    name = "stopped"
    def press_play(self): return Playing()
class Playing:
    name = "playing"
    def press_play(self): return Paused()
class Paused:
    name = "paused"
    def press_play(self): return Playing()

p = Player()
print([p.press_play() for _ in range(4)])               # ['playing', 'paused', 'playing', 'paused']
