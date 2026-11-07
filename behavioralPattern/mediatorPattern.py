"""Mediator pattern: runnable example.

A Mediator is a go-between: instead of many objects talking to each other directly (and each knowing all the others), they all talk only to the mediator, which decides who needs to know what.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/mediator.md

Run it:  python mediatorPattern.py
"""

class ChatRoom:                                         # the mediator
    def __init__(self):
        self.users = {}
    def join(self, user):
        self.users[user.name] = user
        user.room = self
    def send(self, sender, text, to=None):
        if to:
            targets = [self.users[to]]                  # private message
        else:
            targets = [u for n, u in self.users.items() if n != sender.name]    # broadcast
        for u in targets:
            u.receive(sender.name, text)

class User:                                             # a colleague: knows only the room
    def __init__(self, name):
        self.name, self.inbox, self.room = name, [], None
    def say(self, text, to=None):
        self.room.send(self, text, to)
    def receive(self, sender, text):
        self.inbox.append(f"{sender}: {text}")

room = ChatRoom()
ana, bo, cy = User("ana"), User("bo"), User("cy")
for u in (ana, bo, cy):
    room.join(u)
ana.say("hi all")
bo.say("psst", to="cy")
print(bo.inbox)                                         # ['ana: hi all']
print(cy.inbox)                                         # ['ana: hi all', 'bo: psst']

class Checkbox:
    def __init__(self, mediator):
        self.mediator, self.checked = mediator, False
    def toggle(self):
        self.checked = not self.checked
        self.mediator.notify(self, "toggled")

class Button:
    def __init__(self):
        self.enabled = False

class Dialog:                                           # the mediator holds the interaction logic
    def __init__(self):
        self.agree = Checkbox(self)
        self.submit = Button()
    def notify(self, sender, event):
        if sender is self.agree and event == "toggled":
            self.submit.enabled = self.agree.checked    # the rule lives in ONE place

d = Dialog()
print(d.submit.enabled)                                 # False
d.agree.toggle(); print(d.submit.enabled)               # True
d.agree.toggle(); print(d.submit.enabled)               # False

class EventBus:
    def __init__(self):
        self.subscribers = {}
    def subscribe(self, topic, fn):
        self.subscribers.setdefault(topic, []).append(fn)
    def publish(self, topic, payload):
        for fn in self.subscribers.get(topic, []):
            fn(payload)

bus, received = EventBus(), []
bus.subscribe("order.created", lambda o: received.append(f"inventory reserves {o}"))
bus.subscribe("order.created", lambda o: received.append(f"email confirms {o}"))
bus.publish("order.created", "order-1")
print(received)                                         # ['inventory reserves order-1', 'email confirms order-1']
