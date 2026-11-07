"""Flyweight pattern: runnable example.

A Flyweight saves memory by sharing the data that many objects have in common instead of storing a copy in every object.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/flyweight.md

Run it:  python flyweightPattern.py
"""

class Species:                                          # the flyweight: shared, immutable
    __slots__ = ("name", "texture")
    def __init__(self, name, texture):
        self.name, self.texture = name, texture

class SpeciesFactory:                                   # makes sure each species exists once
    _cache = {}
    @classmethod
    def get(cls, name):
        if name not in cls._cache:
            cls._cache[name] = Species(name, texture=f"<2MB texture for {name}>")
        return cls._cache[name]

class Tree:                                             # per-tree (extrinsic) data + a shared reference
    __slots__ = ("x", "y", "species")
    def __init__(self, x, y, species):
        self.x, self.y, self.species = x, y, species

kinds = ("oak", "pine", "fir")
forest = [Tree(i % 500, i // 500, SpeciesFactory.get(kinds[i % 3])) for i in range(60_000)]

print(len(forest), len({id(t.species) for t in forest}), len(SpeciesFactory._cache))
# 60000 3 3     (60,000 trees share just 3 species objects)
print(SpeciesFactory.get("oak") is forest[0].species)   # True

import sys

class HeavyTree:                                        # no sharing: every tree has its own species data
    def __init__(self, x, y, name):
        self.x, self.y, self.name, self.texture = x, y, name, "T" * 2000

class LightTree:                                        # shares the species flyweight
    __slots__ = ("x", "y", "species")
    def __init__(self, x, y, species): self.x, self.y, self.species = x, y, species

heavy = [HeavyTree(i, i, "oak") for i in range(1000)]
shared = SpeciesFactory.get("oak")
light = [LightTree(i, i, shared) for i in range(1000)]

heavy_bytes = sum(sys.getsizeof(t) + sys.getsizeof(t.texture) + sys.getsizeof(t.__dict__) for t in heavy)
light_bytes = sum(sys.getsizeof(t) for t in light)
print(light_bytes < heavy_bytes / 5)                    # True
