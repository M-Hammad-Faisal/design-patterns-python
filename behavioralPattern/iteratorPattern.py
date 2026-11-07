"""Iterator pattern: runnable example.

An Iterator lets you walk through the items of a collection one at a time without knowing (or caring) how the collection stores them: list, tree, database cursor, file, network stream.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/iterator.md

Run it:  python iteratorPattern.py
"""

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):                                 # called by for / list() / sum() ...
        return CountdownIterator(self.start)

class CountdownIterator:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration                         # signals "no more items"
        self.n -= 1
        return self.n + 1

c = Countdown(3)
print(list(c), list(c))                                 # [3, 2, 1] [3, 2, 1]   (fresh iterator each time: reusable)

class Countdown2:
    def __init__(self, start): self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n                                     # yield makes this function an iterator factory
            n -= 1

print(list(Countdown2(4)), sum(Countdown2(4)))          # [4, 3, 2, 1] 10

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

    def __iter__(self):                                 # in-order traversal
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def level_order(self):                              # a second way to traverse the same tree
        queue = [self]
        while queue:
            node = queue.pop(0)
            yield node.value
            queue.extend(n for n in (node.left, node.right) if n)

t = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
print(list(t), sum(t), max(t))                          # [1, 2, 3, 4, 5, 6, 7] 28 7
print(list(t.level_order()))                            # [4, 2, 6, 1, 3, 5, 7]

from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:                                         # infinite, but only computed on demand
        yield a
        a, b = b, a + b

print(list(islice(fibonacci(), 10)))                    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def batched(iterable, n):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == n:
            yield batch
            batch = []
    if batch:
        yield batch

print(list(batched(range(7), 3)))                       # [[0, 1, 2], [3, 4, 5], [6]]

nums = [1, 2, 3]
it = iter(nums)                                         # an iterator over the list
print(list(it), list(it))                               # [1, 2, 3] []   (an iterator is single use)
print(list(nums), list(nums))                           # [1, 2, 3] [1, 2, 3]   (the list is reusable)
