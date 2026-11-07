"""Chain of Responsibility pattern: runnable example.

A request travels along a chain of handlers.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/chain-of-responsibility.md

Run it:  python chainOfResponsibilityPattern.py
"""

class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, request):
        if self.can_handle(request):
            return self.process(request)
        if self.next:
            return self.next.handle(request)             # pass it along
        return f"no handler for {request!r}"

    def can_handle(self, request): raise NotImplementedError
    def process(self, request): raise NotImplementedError

class AuthHandler(Handler):
    def can_handle(self, r): return not r.get("user")
    def process(self, r): return "401 unauthenticated"

class RateLimitHandler(Handler):
    def can_handle(self, r): return r.get("calls", 0) > 100
    def process(self, r): return "429 too many requests"

class AppHandler(Handler):
    def can_handle(self, r): return True
    def process(self, r): return f"200 hello {r['user']}"

chain = AuthHandler(RateLimitHandler(AppHandler()))
print(chain.handle({}))                                  # 401 unauthenticated
print(chain.handle({"user": "ana", "calls": 500}))       # 429 too many requests
print(chain.handle({"user": "ana", "calls": 3}))         # 200 hello ana

def logging_middleware(next_fn):
    def handler(request):
        print("log:", request["path"])
        return next_fn(request)
    return handler

def auth_middleware(next_fn):
    def handler(request):
        if request.get("user") != "admin":
            return "403 forbidden"
        return next_fn(request)
    return handler

def view(request):
    return f"200 secret page {request['path']}"

app = logging_middleware(auth_middleware(view))          # build the chain by wrapping
print(app({"path": "/a", "user": "admin"}))              # log: /a   then   200 secret page /a
print(app({"path": "/b", "user": "bob"}))                # log: /b   then   403 forbidden

import re

def not_empty(d):      return None if d.get("name") else "name is required"
def valid_email(d):    return None if re.fullmatch(r"[^@\s]+@[^@\s]+\.\w+", d.get("email", "")) else "invalid email"
def long_password(d):  return None if len(d.get("password", "")) >= 8 else "password too short"

def validate(data, chain=(not_empty, valid_email, long_password)):
    for check in chain:
        error = check(data)
        if error:
            return error                                 # first failing handler stops the chain
    return "ok"

print(validate({"name": "a", "email": "a@x.com", "password": "12345678"}))     # ok
print(validate({"name": "a", "email": "bad"}))                                  # invalid email
