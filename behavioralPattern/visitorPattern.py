"""Visitor pattern: runnable example.

A Visitor lets you add new operations to a set of classes without modifying those classes.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/visitor.md

Run it:  python visitorPattern.py
"""

class Num:
    def __init__(self, value): self.value = value
    def accept(self, visitor): return visitor.visit_num(self)

class Add:
    def __init__(self, left, right): self.left, self.right = left, right
    def accept(self, visitor): return visitor.visit_add(self)

class Mul:
    def __init__(self, left, right): self.left, self.right = left, right
    def accept(self, visitor): return visitor.visit_mul(self)

class Evaluator:                                        # operation 1
    def visit_num(self, n): return n.value
    def visit_add(self, n): return n.left.accept(self) + n.right.accept(self)
    def visit_mul(self, n): return n.left.accept(self) * n.right.accept(self)

class Printer:                                          # operation 2
    def visit_num(self, n): return str(n.value)
    def visit_add(self, n): return f"({n.left.accept(self)} + {n.right.accept(self)})"
    def visit_mul(self, n): return f"{n.left.accept(self)} * {n.right.accept(self)}"

expr = Mul(Add(Num(2), Num(3)), Num(4))
print(expr.accept(Printer()), "=", expr.accept(Evaluator()))     # (2 + 3) * 4 = 20

class DepthCounter:                                     # operation 3, added WITHOUT touching Num/Add/Mul
    def visit_num(self, n): return 1
    def visit_add(self, n): return 1 + max(n.left.accept(self), n.right.accept(self))
    def visit_mul(self, n): return 1 + max(n.left.accept(self), n.right.accept(self))

print(expr.accept(DepthCounter()))                      # 3
