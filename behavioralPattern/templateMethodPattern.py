"""Template Method pattern: runnable example.

Template Method fixes the order of the steps of an algorithm in a base class, and lets subclasses fill in or change individual steps without changing the order.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/template-method.md

Run it:  python templateMethodPattern.py
"""

from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def generate(self, data):                           # the template method: fixed order
        rows = self.collect(data)
        body = self.format(rows)
        return self.header() + body + self.footer()

    @abstractmethod
    def collect(self, data): ...                        # required step

    @abstractmethod
    def format(self, rows): ...                         # required step

    def header(self): return ""                         # optional "hook" with a default
    def footer(self): return ""

class CsvReport(ReportGenerator):
    def collect(self, data):
        return sorted(data.items())
    def format(self, rows):
        return "\n".join(f"{k},{v}" for k, v in rows)
    def header(self):
        return "key,value\n"

class HtmlReport(ReportGenerator):
    def collect(self, data):
        return sorted(data.items())
    def format(self, rows):
        return "".join(f"<li>{k}: {v}</li>" for k, v in rows)
    def header(self): return "<ul>"
    def footer(self): return "</ul>"

data = {"b": 2, "a": 1}
print(CsvReport().generate(data))
# key,value
# a,1
# b,2
print(HtmlReport().generate(data))                      # <ul><li>a: 1</li><li>b: 2</li></ul>

class DataPipeline(ABC):
    def run(self):
        rows = self.transform(self.extract())
        if not self.validate(rows):
            raise ValueError("invalid data")
        return self.load(rows)

    @abstractmethod
    def extract(self): ...
    @abstractmethod
    def transform(self, rows): ...
    @abstractmethod
    def load(self, rows): ...
    def validate(self, rows): return True               # hook

class Doubler(DataPipeline):
    def extract(self): return [1, 2, 3]
    def transform(self, rows): return [r * 2 for r in rows]
    def load(self, rows): return sum(rows)

class StrictDoubler(Doubler):
    def validate(self, rows): return all(r > 100 for r in rows)

print(Doubler().run())                                  # 12
try:
    StrictDoubler().run()
except ValueError as e:
    print(e)                                            # invalid data
