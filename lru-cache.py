""" As of 09/21/2020 21:17 MST
    Runtime: 248 ms (beats 38.91% of python3 submissions)
    Memory: 23 MB (beats 67.67% of python3 submissions)
    Overall: Not impressive buddy...
"""
from Library.DoublyConnectedLinkedList import DoublyConnectedLinkedList as LinkedList


class LRUCache:
    def __init__(self, capacity):
        self.storage = {}
        self.usage = LinkedList()

        self.capacity = capacity

        self.KEY = 0
        self.VALUE = 1

    def get(self, key):
        if key in self.storage:
            n_value = self.storage[key]
            self.usage.moveToTail(n_value)

            return n_value.getValue()[self.VALUE]
        else:
            return -1

    def put(self, key, value):
        if key not in self.storage:
            if len(self.storage) >= self.capacity:
                n_removed = self.usage.popHead()
                self.storage.pop(n_removed.getValue()[self.KEY])

            n = self.usage.addTail({self.KEY: key, self.VALUE: value})
            self.storage[key] = n
        else:
            n_value = self.storage[key]
            self.usage.moveToTail(n_value)
            n_value.updateValue(value)

        return self

    def __repr__(self):
        return self.usage.__repr__()


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
