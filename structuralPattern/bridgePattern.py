"""Bridge pattern: runnable example.

A Bridge splits a design into two separate hierarchies (what something *is* versus how it is *done*) and connects them with a reference, so each side can grow independently.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/bridge.md

Run it:  python bridgePattern.py
"""

from abc import ABC, abstractmethod

class Renderer(ABC):                                    # the implementation hierarchy
    @abstractmethod
    def circle(self, r): ...
    @abstractmethod
    def square(self, side): ...

class SvgRenderer(Renderer):
    def circle(self, r): return f'<circle r="{r}"/>'
    def square(self, side): return f'<rect width="{side}" height="{side}"/>'

class AsciiRenderer(Renderer):
    def circle(self, r): return f"(circle of radius {r})"
    def square(self, side): return f"[square of side {side}]"

class Shape:                                            # the abstraction hierarchy
    def __init__(self, renderer: Renderer):
        self.renderer = renderer                        # <- the "bridge"

class Circle(Shape):
    def __init__(self, renderer, r):
        super().__init__(renderer)
        self.r = r
    def draw(self):
        return self.renderer.circle(self.r)

class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side
    def draw(self):
        return self.renderer.square(self.side)

for renderer in (SvgRenderer(), AsciiRenderer()):
    print(Circle(renderer, 2).draw(), "|", Square(renderer, 3).draw())
# <circle r="2"/> | <rect width="3" height="3"/>
# (circle of radius 2) | [square of side 3]

class Channel(ABC):
    @abstractmethod
    def deliver(self, text): ...

class Email(Channel):
    def deliver(self, text): return f"EMAIL: {text}"

class Sms(Channel):
    def deliver(self, text): return f"SMS: {text}"

class Message:
    def __init__(self, channel): self.channel = channel

class Alert(Message):
    def send(self, text): return self.channel.deliver("ALERT " + text)

class Report(Message):
    def send(self, text): return self.channel.deliver("REPORT " + text)

print(Alert(Email()).send("disk full"), "|", Report(Sms()).send("daily summary"))
# EMAIL: ALERT disk full | SMS: REPORT daily summary
