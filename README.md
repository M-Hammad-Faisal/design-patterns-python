# Design Patterns in Python

Runnable Python examples of the classic **Gang of Four (GoF)** design patterns, plus two widely used extras (Object Pool and Null Object).

> **New to patterns or the jargon?** (What is "GoF"? What does "creational" mean?) Read the plain-English guide first:
> **[Design Patterns: A Plain-English Guide](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/README.md)**
> Every pattern below has its own detailed lesson (analogy, the problem, step-by-step code, the Pythonic shortcut, pros and cons, real-world examples, exercises with solutions). This repository is the place to **run and tinker**; the lessons are the place to **understand**.

## What "GoF" means

The *Gang of Four* are the four authors of the 1994 book *Design Patterns*. It named **23 patterns** that experienced developers kept reusing, in three families:

- **Creational**: how objects are created (Singleton, Factory Method, Abstract Factory, Builder, Prototype).
- **Structural**: how objects are put together (Adapter, Decorator, Proxy, Facade, Composite, Bridge, Flyweight).
- **Behavioral**: how objects communicate and share work (Strategy, Observer, Command, State, Template Method, Iterator, Chain of Responsibility, Mediator, Memento, Visitor, Interpreter).

## The patterns

| Family | Pattern | Script | Detailed lesson |
|--------|---------|--------|-----------------|
| Creational | Singleton | [`creationalPattern/singletonPattern.py`](creationalPattern/singletonPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/singleton.md) |
| Creational | Factory Method | [`creationalPattern/factoryPattern.py`](creationalPattern/factoryPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/factory-method.md) |
| Creational | Abstract Factory | [`creationalPattern/abstractFactoryPattern.py`](creationalPattern/abstractFactoryPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/abstract-factory.md) |
| Creational | Builder | [`creationalPattern/builderPattern.py`](creationalPattern/builderPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/builder.md) |
| Creational | Prototype | [`creationalPattern/prototypePattern.py`](creationalPattern/prototypePattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/prototype.md) |
| Creational | Object Pool (extra) | [`creationalPattern/objectPoolPattern.py`](creationalPattern/objectPoolPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/object-pool.md) |
| Structural | Adapter | [`structuralPattern/adapterPattern.py`](structuralPattern/adapterPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/adapter.md) |
| Structural | Decorator | [`structuralPattern/decoratorPattern.py`](structuralPattern/decoratorPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/decorator.md) |
| Structural | Composite | [`structuralPattern/compositePattern.py`](structuralPattern/compositePattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/composite.md) |
| Structural | Proxy | [`structuralPattern/proxyPattern.py`](structuralPattern/proxyPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/proxy.md) |
| Structural | Facade | [`structuralPattern/facadePattern.py`](structuralPattern/facadePattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/facade.md) |
| Structural | Bridge | [`structuralPattern/bridgePattern.py`](structuralPattern/bridgePattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/bridge.md) |
| Structural | Flyweight | [`structuralPattern/flyweightPattern.py`](structuralPattern/flyweightPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/structural/flyweight.md) |
| Behavioral | Strategy | [`behavioralPattern/strategyPattern.py`](behavioralPattern/strategyPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/strategy.md) |
| Behavioral | Observer | [`behavioralPattern/observerPattern.py`](behavioralPattern/observerPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/observer.md) |
| Behavioral | Command | [`behavioralPattern/commandPattern.py`](behavioralPattern/commandPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/command.md) |
| Behavioral | State | [`behavioralPattern/statePattern.py`](behavioralPattern/statePattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/state.md) |
| Behavioral | Template Method | [`behavioralPattern/templateMethodPattern.py`](behavioralPattern/templateMethodPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/template-method.md) |
| Behavioral | Iterator | [`behavioralPattern/iteratorPattern.py`](behavioralPattern/iteratorPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/iterator.md) |
| Behavioral | Chain of Responsibility | [`behavioralPattern/chainOfResponsibilityPattern.py`](behavioralPattern/chainOfResponsibilityPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/chain-of-responsibility.md) |
| Behavioral | Mediator | [`behavioralPattern/mediatorPattern.py`](behavioralPattern/mediatorPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/mediator.md) |
| Behavioral | Memento | [`behavioralPattern/mementoPattern.py`](behavioralPattern/mementoPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/memento.md) |
| Behavioral | Visitor | [`behavioralPattern/visitorPattern.py`](behavioralPattern/visitorPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/visitor.md) |
| Behavioral | Interpreter | [`behavioralPattern/interpreterPattern.py`](behavioralPattern/interpreterPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/interpreter.md) |
| Behavioral | Null Object (extra) | [`behavioralPattern/nullObjectPattern.py`](behavioralPattern/nullObjectPattern.py) | [lesson](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/behavioral/null-object.md) |

## Running the examples

Each script is self-contained and uses only the standard library (Python 3.10+):

```bash
python creationalPattern/builderPattern.py
python behavioralPattern/observerPattern.py
```

Run every script and check that they all succeed:

```bash
python run_all.py
```

## How to study a pattern

1. Read its lesson (the "In plain words" and "The problem" sections first).
2. Run the script and read the output.
3. Change something: add a new strategy, a new state, a new decorator. Notice what you did *not* have to edit.
4. Do the exercises at the end of the lesson.

## Related

- The full handbook (data structures, algorithms, OOP, databases, operating systems, networking, modern Python): [cs-fundamentals-handbook](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook)
- OOP foundations behind the patterns: [classes](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/classes-objects/README.md), [inheritance](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/inheritance-mro/README.md), [composition](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/composition-design/README.md), [SOLID](https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/solid/README.md).
