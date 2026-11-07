"""Facade pattern: runnable example.

A Facade is one simple entry point in front of a complicated system.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/facade.md

Run it:  python facadePattern.py
"""

class VideoDecoder:
    def decode(self, f): return f"frames({f})"

class AudioExtractor:
    def extract(self, f): return f"audio({f})"

class Compressor:
    def compress(self, data, quality): return f"{data}@{quality}"

class Muxer:
    def mux(self, video, audio): return f"{video}+{audio}"

class VideoConverter:                                   # the facade
    def convert(self, filename, quality="high"):
        video = Compressor().compress(VideoDecoder().decode(filename), quality)
        audio = AudioExtractor().extract(filename)
        return Muxer().mux(video, audio)

print(VideoConverter().convert("movie.avi"))            # frames(movie.avi)@high+audio(movie.avi)
print(VideoConverter().convert("clip.mp4", "low"))      # frames(clip.mp4)@low+audio(clip.mp4)

class Inventory:
    def __init__(self): self.stock = {"pen": 5}
    def reserve(self, sku, qty):
        if self.stock.get(sku, 0) < qty:
            raise ValueError(f"not enough {sku}")
        self.stock[sku] -= qty

class Payments:
    def charge(self, user, amount): return f"charged {user} {amount}"

class Shipping:
    def book(self, user, sku): return f"shipping {sku} to {user}"

class CheckoutFacade:
    def __init__(self, inventory, payments, shipping):
        self.inventory, self.payments, self.shipping = inventory, payments, shipping
    def buy(self, user, sku, qty, price):
        self.inventory.reserve(sku, qty)                # step 1
        receipt = self.payments.charge(user, price * qty)    # step 2
        label = self.shipping.book(user, sku)           # step 3
        return receipt, label

shop = CheckoutFacade(Inventory(), Payments(), Shipping())
print(shop.buy("ana", "pen", 2, 3))                     # ('charged ana 6', 'shipping pen to ana')
