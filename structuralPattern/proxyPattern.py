"""Proxy pattern: runnable example.

A Proxy is a stand-in for another object.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/proxy.md

Run it:  python proxyPattern.py
"""

class Image:                                           # the real subject
    def __init__(self, path):
        self.path = path
        print(f"loading {path} from disk (slow)")
    def draw(self):
        return f"drawing {self.path}"

class LazyImage:                                       # the proxy: same interface (draw)
    def __init__(self, path):
        self.path, self._real = path, None
    def draw(self):
        if self._real is None:
            self._real = Image(self.path)              # created only on first use
        return self._real.draw()

gallery = [LazyImage(f"{i}.png") for i in range(1000)]   # instant: nothing loaded yet
print(gallery[7].draw())     # loading 7.png from disk (slow) / drawing 7.png
print(gallery[7].draw())     # drawing 7.png  (already loaded; no second load)

class SecureImage:
    def __init__(self, image, roles):
        self.image, self.roles = image, roles
    def draw(self):
        if "viewer" not in self.roles:
            raise PermissionError("not allowed")
        return self.image.draw()

print(SecureImage(gallery[1], ["viewer"]).draw())
try:
    SecureImage(gallery[1], ["guest"]).draw()
except PermissionError as e:
    print("denied:", e)                                 # denied: not allowed

class WeatherService:
    def forecast(self, city):
        return f"sunny in {city}"

class CachingWeather:
    def __init__(self, real):
        self.real, self.cache, self.real_calls = real, {}, 0
    def forecast(self, city):
        if city not in self.cache:
            self.real_calls += 1
            self.cache[city] = self.real.forecast(city)
        return self.cache[city]

w = CachingWeather(WeatherService())
w.forecast("Lahore"); w.forecast("Lahore"); w.forecast("Karachi")
print(w.real_calls)                                     # 2

class CountingProxy:
    def __init__(self, target):
        self._target, self.calls = target, {}
    def __getattr__(self, name):                        # called for names the proxy itself lacks
        attr = getattr(self._target, name)
        if callable(attr):
            def wrapper(*a, **kw):
                self.calls[name] = self.calls.get(name, 0) + 1
                return attr(*a, **kw)
            return wrapper
        return attr

p = CountingProxy([3, 1, 2])
p.sort(); p.append(9); p.append(10)
print(p.calls)                                          # {'sort': 1, 'append': 2}
