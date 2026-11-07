"""Object Pool pattern: runnable example.

An Object Pool keeps a fixed set of expensive objects ready to be borrowed and returned, instead of creating and destroying them each time.

Full lesson (explanation, pros and cons, exercises):
https://github.com/M-Hammad-Faisal/cs-fundamentals-handbook/blob/main/04-oop/design-patterns/creational/object-pool.md

Run it:  python objectPoolPattern.py
"""

import queue
import threading
from contextlib import contextmanager

class Connection:
    created = 0
    def __init__(self):
        Connection.created += 1
        self.id = Connection.created
    def query(self, sql):
        return f"conn{self.id}: {sql}"

class PoolExhausted(Exception):
    pass

class Pool:
    def __init__(self, size):
        self._free = queue.Queue()
        for _ in range(size):
            self._free.put(Connection())

    @contextmanager
    def acquire(self, timeout=1.0):
        try:
            conn = self._free.get(timeout=timeout)       # blocks while the pool is empty
        except queue.Empty:
            raise PoolExhausted("no connection available") from None
        try:
            yield conn
        finally:
            self._free.put(conn)                         # ALWAYS return it, even on error

pool = Pool(2)
used = []
for _ in range(5):
    with pool.acquire() as c:
        used.append(c.id)
print(used, Connection.created)       # [1, 2, 1, 2, 1] 2   (5 uses, only 2 connections ever created)

# Many threads sharing a small pool
results = []
lock = threading.Lock()
def worker(n):
    with pool.acquire(timeout=2) as c:
        with lock:
            results.append(c.query(f"SELECT {n}"))
threads = [threading.Thread(target=worker, args=(i,)) for i in range(6)]
for t in threads: t.start()
for t in threads: t.join()
print(len(results), Connection.created)   # 6 2

tiny = Pool(1)
with tiny.acquire():
    try:
        with tiny.acquire(timeout=0.1):
            pass
    except PoolExhausted as e:
        print("second borrower:", e)                      # second borrower: no connection available
