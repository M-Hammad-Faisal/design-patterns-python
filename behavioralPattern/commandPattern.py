"""Command pattern: runnable example.

A Command turns a request into an object.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/command.md

Run it:  python commandPattern.py
"""

class TextEditor:                                       # the receiver
    def __init__(self):
        self.text = ""

class InsertCommand:
    def __init__(self, editor, s):
        self.editor, self.s = editor, s
    def execute(self):
        self.editor.text += self.s
    def undo(self):
        self.editor.text = self.editor.text[:-len(self.s)]

class DeleteLastCommand:
    def __init__(self, editor, n):
        self.editor, self.n, self.removed = editor, n, ""
    def execute(self):
        self.removed = self.editor.text[-self.n:]       # remember what we remove, so undo can restore it
        self.editor.text = self.editor.text[:-self.n]
    def undo(self):
        self.editor.text += self.removed

class History:                                          # the invoker
    def __init__(self):
        self._done, self._undone = [], []
    def run(self, command):
        command.execute()
        self._done.append(command)
        self._undone.clear()                            # a new action invalidates the redo stack
    def undo(self):
        if self._done:
            cmd = self._done.pop()
            cmd.undo()
            self._undone.append(cmd)
    def redo(self):
        if self._undone:
            cmd = self._undone.pop()
            cmd.execute()
            self._done.append(cmd)

editor, history = TextEditor(), History()
history.run(InsertCommand(editor, "Hello"))
history.run(InsertCommand(editor, " world"))
history.run(DeleteLastCommand(editor, 3))
print(repr(editor.text))                                # 'Hello wo'
history.undo(); print(repr(editor.text))                # 'Hello world'
history.undo(); print(repr(editor.text))                # 'Hello'
history.redo(); print(repr(editor.text))                # 'Hello world'

import queue

jobs = queue.Queue()
jobs.put(InsertCommand(editor, "!"))
jobs.put(InsertCommand(editor, "?"))
while not jobs.empty():
    jobs.get().execute()                                # executed later, perhaps by another worker
print(editor.text)                                      # Hello world!?

class MacroCommand:
    def __init__(self, *commands):
        self.commands = commands
    def execute(self):
        for c in self.commands: c.execute()
    def undo(self):
        for c in reversed(self.commands): c.undo()      # undo in reverse order

ed2 = TextEditor()
macro = MacroCommand(InsertCommand(ed2, "a"), InsertCommand(ed2, "b"), InsertCommand(ed2, "c"))
macro.execute(); print(ed2.text)                        # abc
macro.undo(); print(repr(ed2.text))                     # ''
