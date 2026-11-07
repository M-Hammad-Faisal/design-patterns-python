"""Observer pattern: runnable example.

With Observer, one object (the subject or publisher) keeps a list of others (the observers or subscribers) and notifies all of them automatically when something happens.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/observer.md

Run it:  python observerPattern.py
"""

class EventEmitter:
    def __init__(self):
        self._handlers = {}                                   # event name -> list of callbacks

    def subscribe(self, event, handler):
        self._handlers.setdefault(event, []).append(handler)
        return lambda: self._handlers[event].remove(handler)  # returns an "unsubscribe" function

    def emit(self, event, *args):
        for handler in list(self._handlers.get(event, [])):   # iterate a copy: handlers may unsubscribe
            handler(*args)

class Stock:                                                  # the subject
    def __init__(self, symbol, price):
        self.symbol, self._price = symbol, price
        self.events = EventEmitter()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        old, self._price = self._price, value
        self.events.emit("price_changed", self.symbol, old, value)

log = []
stock = Stock("ACME", 100)
unsubscribe_chart = stock.events.subscribe(
    "price_changed", lambda s, o, n: log.append(f"chart: {s} {o}->{n}"))
stock.events.subscribe(
    "price_changed", lambda s, o, n: n > 120 and log.append(f"alert: {s} spiked to {n}"))

stock.price = 110
stock.price = 130
unsubscribe_chart()                                           # chart stops listening
stock.price = 90
print(log)
# ['chart: ACME 100->110', 'chart: ACME 110->130', 'alert: ACME spiked to 130']

class Subject:
    def __init__(self): self._observers = []
    def attach(self, o): self._observers.append(o)
    def detach(self, o): self._observers.remove(o)
    def notify(self, data):
        for o in self._observers:
            o.update(data)

class Display:
    def __init__(self, name): self.name, self.seen = name, []
    def update(self, data): self.seen.append(data)

weather = Subject()
d1, d2 = Display("phone"), Display("web")
weather.attach(d1); weather.attach(d2)
weather.notify("rain"); weather.detach(d2); weather.notify("sun")
print(d1.seen, d2.seen)                                       # ['rain', 'sun'] ['rain']

def safe_emit(handlers, *args):
    errors = []
    for h in handlers:
        try:
            h(*args)
        except Exception as e:                                # isolate failures
            errors.append(type(e).__name__)
    return errors

def broken(x): raise RuntimeError
ok = []
print(safe_emit([broken, ok.append], 5), ok)                   # ['RuntimeError'] [5]
