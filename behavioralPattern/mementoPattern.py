"""Memento pattern: runnable example.

A Memento is a saved snapshot of an object's state that lets you restore it later, without exposing the object's private internals.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/memento.md

Run it:  python mementoPattern.py
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Snapshot:                                         # the memento: immutable
    text: str
    cursor: int

class Document:                                         # the originator
    def __init__(self):
        self.text, self.cursor = "", 0

    def type(self, s):
        self.text = self.text[:self.cursor] + s + self.text[self.cursor:]
        self.cursor += len(s)

    def save(self):
        return Snapshot(self.text, self.cursor)         # create a snapshot

    def restore(self, snapshot):
        self.text, self.cursor = snapshot.text, snapshot.cursor

doc = Document()
checkpoints = []                                        # the caretaker
doc.type("hello");  checkpoints.append(doc.save())
doc.type(" world"); checkpoints.append(doc.save())
doc.type("!!!")
print(doc.text)                                         # hello world!!!
doc.restore(checkpoints[0])
print(doc.text, doc.cursor)                             # hello 5

from collections import deque

class Editor:
    def __init__(self, max_history=3):
        self.doc = Document()
        self.history = deque(maxlen=max_history)        # old snapshots fall off the far end

    def type(self, s):
        self.history.append(self.doc.save())            # snapshot BEFORE changing
        self.doc.type(s)

    def undo(self):
        if self.history:
            self.doc.restore(self.history.pop())

e = Editor()
for word in ("a", "b", "c", "d"):
    e.type(word)
print(e.doc.text)                                       # abcd
e.undo(); e.undo(); e.undo()
print(e.doc.text)                                       # a   (only the last 3 steps could be undone)
e.undo()
print(e.doc.text)                                       # a   (nothing more to undo)
