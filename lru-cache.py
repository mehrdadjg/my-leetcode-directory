class LRUCache:
    class Node:
        def __init__(self, key, value, prev, next):
            self.key = key
            self.value = value
            self.next = next
            self.prev = prev

        def __repr__(self):
            return "({}: {}) -> {}".format(self.key, self.value, self.next)

        def setNext(self, next):
            self.next = next

        def getNext(self):
            return self.next

        def setPrev(self, prev):
            self.prev = prev

        def getPrev(self):
            return self.prev

        def updateValue(self, value):
            self.value = value

        def getValue(self):
            return self.value

    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def __repr__(self):
            return self.head.__repr__()

        def addHead(self, key, value):
            n = LRUCache.Node(key, value, None, self.head)
            if self.head == None:
                self.tail = n
            else:
                self.head.setPrev(n)

            self.head = n
            return n

        def addTail(self, key, value):
            n = LRUCache.Node(key, value, self.tail, None)
            if self.tail == None:
                self.head = n
            else:
                self.tail.setNext(n)

            self.tail = n
            return n

        def moveToTail(self, n):
            if self.tail == n:
                return self.tail

            if self.head == n:
                self.head.setPrev(self.tail)
                self.head = n.getNext()
                self.head.setPrev(None)
                self.tail.setNext(n)
                self.tail = n
                self.tail.setNext(None)
            else:
                n.prev.setNext(n.getNext())
                n.next.setPrev(n.getPrev())
                n.setNext(None)
                n.setPrev(self.tail)
                self.tail.setNext(n)
                self.tail = n

            return self.tail

        def popHead(self):
            if self.head == None:
                raise Exception("Linked list is empty")

            if self.head == self.tail:
                self.tail = None

            n = self.head
            self.head = n.getNext()
            if self.head != None:
                self.head.setPrev(None)

            return n

    def __init__(self, capacity):
        self.storage = {}
        self.usage = LRUCache.LinkedList()

        self.capacity = capacity

    def get(self, key):
        if key in self.storage:
            n_value = self.storage[key]
            self.usage.moveToTail(n_value)

            return n_value.getValue()
        else:
            return -1

    def put(self, key, value):
        if key not in self.storage:
            if len(self.storage) >= self.capacity:
                n_removed = self.usage.popHead()
                self.storage.pop(n_removed.key)

            n = self.usage.addTail(key, value)
            self.storage[key] = n
        else:
            n_value = self.storage[key]
            self.usage.moveToTail(n_value)
            n_value.updateValue(value)

        return self

    def __repr__(self):
        return self.usage.__repr__()


lru = LRUCache(1)
print(lru.put(2, 1))
print(lru.get(2))
print(lru.put(3, 2))
