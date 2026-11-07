"""Interpreter pattern: runnable example.

The Interpreter pattern defines a small language (a grammar) as classes and evaluates sentences of that language by building a tree of objects, where each object knows how to compute its own meaning.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/interpreter.md

Run it:  python interpreterPattern.py
"""

class Expression:
    def interpret(self, ctx):
        raise NotImplementedError

class Const(Expression):
    def __init__(self, value): self.value = value
    def interpret(self, ctx): return self.value

class Var(Expression):
    def __init__(self, name): self.name = name
    def interpret(self, ctx): return ctx[self.name]

class Greater(Expression):
    def __init__(self, left, right): self.left, self.right = left, right
    def interpret(self, ctx): return self.left.interpret(ctx) > self.right.interpret(ctx)

class Equals(Expression):
    def __init__(self, left, right): self.left, self.right = left, right
    def interpret(self, ctx): return self.left.interpret(ctx) == self.right.interpret(ctx)

class And(Expression):
    def __init__(self, left, right): self.left, self.right = left, right
    def interpret(self, ctx): return self.left.interpret(ctx) and self.right.interpret(ctx)

class Or(Expression):
    def __init__(self, left, right): self.left, self.right = left, right
    def interpret(self, ctx): return self.left.interpret(ctx) or self.right.interpret(ctx)

rule = And(Greater(Var("age"), Const(18)), Equals(Var("country"), Const("PK")))
print(rule.interpret({"age": 21, "country": "PK"}))     # True
print(rule.interpret({"age": 16, "country": "PK"}))     # False
print(rule.interpret({"age": 30, "country": "US"}))     # False

import re

def tokenize(text):
    return re.findall(r"\d+|[A-Za-z_]+|[+\-*/()]", text)

class Parser:
    """Recursive descent for:  expr = term (('+'|'-') term)* ; term = factor (('*'|'/') factor)* ;
       factor = NUMBER | NAME | '(' expr ')'"""
    def __init__(self, text):
        self.tokens, self.pos = tokenize(text), 0
    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    def take(self):
        tok = self.tokens[self.pos]; self.pos += 1; return tok
    def expr(self):
        node = self.term()
        while self.peek() in ("+", "-"):
            node = BinOp(self.take(), node, self.term())
        return node
    def term(self):
        node = self.factor()
        while self.peek() in ("*", "/"):
            node = BinOp(self.take(), node, self.factor())
        return node
    def factor(self):
        tok = self.take()
        if tok == "(":
            node = self.expr(); self.take(); return node          # consume ")"
        return Const(int(tok)) if tok.isdigit() else Var(tok)

class BinOp(Expression):
    OPS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b, "/": lambda a, b: a / b}
    def __init__(self, op, left, right): self.op, self.left, self.right = op, left, right
    def interpret(self, ctx): return self.OPS[self.op](self.left.interpret(ctx), self.right.interpret(ctx))

tree = Parser("price * (1 - discount) + shipping").expr()
print(tree.interpret({"price": 200, "discount": 0, "shipping": 5}))          # 205
print(Parser("2 + 3 * 4").expr().interpret({}), Parser("(2 + 3) * 4").expr().interpret({}))   # 14 20
