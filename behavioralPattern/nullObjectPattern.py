"""Null Object pattern: runnable example.

A Null Object is an object that does nothing, safely, used in place of None so callers never have to check "is it there?" before using it.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/null-object.md

Run it:  python nullObjectPattern.py
"""

class Logger:
    def info(self, msg):
        print("LOG:", msg)

class NullLogger:                                       # same interface, does nothing
    def info(self, msg):
        pass

def process(items, logger=None):
    logger = logger or NullLogger()                     # one place decides; the rest is check-free
    for item in items:
        logger.info(f"processing {item}")
    return len(items)

print(process([1, 2]))                                  # 2   (silent)
print(process([1], Logger()))                           # LOG: processing 1   then   1

class User:
    is_authenticated = True
    def __init__(self, name, permissions):
        self.name, self.permissions = name, set(permissions)
    def can(self, action):
        return action in self.permissions

class AnonymousUser:                                    # the null object
    name = "anonymous"
    is_authenticated = False
    def can(self, action):
        return False

def current_user(session):
    return User(*session["user"]) if "user" in session else AnonymousUser()

def render_header(session):
    user = current_user(session)                        # never None
    return f"{user.name} (edit: {user.can('edit')}, logged in: {user.is_authenticated})"

print(render_header({}))                                # anonymous (edit: False, logged in: False)
print(render_header({"user": ("ana", ["edit"])}))       # ana (edit: True, logged in: True)

class NullCart:
    items = ()
    def total(self): return 0
    def __iter__(self): return iter(())
    def __len__(self): return 0

def checkout_summary(cart):
    return f"{len(cart)} items, total {cart.total()}"

print(checkout_summary(NullCart()))                     # 0 items, total 0
