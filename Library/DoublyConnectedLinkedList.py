import unittest


class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return '({}) -> {}'.format(self.value, self.next)

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


class DoublyConnectedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return self.head.__repr__()

    def addHead(self, value):
        n = Node(value, None, self.head)
        if self.head == None:
            self.tail = n
        else:
            self.head.setPrev(n)

        self.head = n
        return n

    def addTail(self, value):
        n = Node(value, self.tail, None)
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
            raise Exception('Linked list is empty.')

        if self.head == self.tail:
            self.tail = None

        n = self.head
        self.head = n.getNext()
        if self.head != None:
            self.head.setPrev(None)

        return n


class TestDoublyConnectedLinkedList(unittest.TestCase):
    def test_initialization(self):
        dcll = DoublyConnectedLinkedList()
        self.assertEqual(dcll.head, None)
        self.assertEqual(dcll.tail, None)

    def test_add_head(self):
        dcll = DoublyConnectedLinkedList()
        dcll.addHead(1)
        self.assertEqual(dcll.head.getValue(), 1)
        self.assertEqual(dcll.tail.getValue(), 1)
        self.assertEqual(dcll.tail.getNext(), None)
        self.assertEqual(dcll.head.getPrev(), None)
        dcll.addHead(2)
        self.assertEqual(dcll.head.getValue(), 2)
        self.assertEqual(dcll.tail.getValue(), 1)
        self.assertEqual(dcll.tail.getPrev(), dcll.head)
        self.assertEqual(dcll.tail.getPrev().getNext(), dcll.tail)
        self.assertEqual(dcll.head.getNext(), dcll.tail)
        dcll.addHead(3)
        self.assertEqual(dcll.head.getValue(), 3)
        self.assertEqual(dcll.tail.getValue(), 1)
        self.assertEqual(dcll.tail.getPrev(), dcll.head.getNext())
        self.assertEqual(dcll.tail.getPrev().getNext(), dcll.tail)

    def test_add_tail(self):
        dcll = DoublyConnectedLinkedList()
        dcll.addTail(1)
        self.assertEqual(dcll.head.getValue(), 1)
        self.assertEqual(dcll.tail.getValue(), 1)
        self.assertEqual(dcll.tail.getNext(), None)
        self.assertEqual(dcll.head.getPrev(), None)
        dcll.addTail(2)
        self.assertEqual(dcll.head.getValue(), 1)
        self.assertEqual(dcll.tail.getValue(), 2)
        self.assertEqual(dcll.tail.getPrev(), dcll.head)
        self.assertEqual(dcll.tail.getPrev().getNext(), dcll.tail)
        self.assertEqual(dcll.head.getNext(), dcll.tail)
        dcll.addTail(3)
        self.assertEqual(dcll.head.getValue(), 1)
        self.assertEqual(dcll.tail.getValue(), 3)
        self.assertEqual(dcll.tail.getPrev(), dcll.head.getNext())
        self.assertEqual(dcll.tail.getPrev().getNext(), dcll.tail)

    def test_add_mix(self):
        dcll = DoublyConnectedLinkedList()
        dcll.addTail(1)
        dcll.addHead(2)
        self.assertEqual(dcll.head.getValue(), 2)
        self.assertEqual(dcll.tail.getValue(), 1)
        self.assertEqual(dcll.head.getNext(), dcll.tail)
        self.assertEqual(dcll.head, dcll.tail.getPrev())
        self.assertEqual(dcll.head.getNext().getPrev(), dcll.head)
        dcll.addHead(3)
        dcll.addTail(4)
        self.assertEqual(dcll.head.getValue(), 3)
        self.assertEqual(dcll.tail.getValue(), 4)

    def test_move_to_tail(self):
        dcll = DoublyConnectedLinkedList()
        dcll.addHead(1)
        dcll.moveToTail(dcll.head)
        self.assertEqual(dcll.tail.getValue(), 1)
        self.assertEqual(dcll.tail.getPrev(), None)
        self.assertEqual(dcll.tail.getNext(), None)
        dcll.addTail(2)
        dcll.moveToTail(dcll.head)
        self.assertEqual(dcll.tail.getValue(), 1)
        self.assertEqual(dcll.tail.getPrev(), dcll.head)
        self.assertEqual(dcll.head.getNext().getValue(), 1)
        dcll.addHead(3)
        dcll.moveToTail(dcll.head.getNext())
        self.assertEqual(dcll.tail.getValue(), 2)

    def test_pop_head(self):
        dcll = DoublyConnectedLinkedList()
        with self.assertRaises(Exception):
            dcll.popHead()

        dcll.addTail(1)
        x = dcll.popHead()
        self.assertEqual(dcll.head, None)
        self.assertEqual(dcll.tail, None)
        self.assertEqual(x.getValue(), 1)
        self.assertEqual(x.getNext(), None)
        self.assertEqual(x.getPrev(), None)

        dcll.addHead(2)
        dcll.addTail(3)
        a = dcll.popHead()
        self.assertEqual(dcll.head.getValue(), 3)
        self.assertEqual(dcll.tail.getValue(), 3)
        b = dcll.popHead()
        self.assertEqual(dcll.head, None)
        self.assertEqual(dcll.tail, None)

        self.assertEqual(a.getValue(), 2)
        self.assertEqual(b.getValue(), 3)
        self.assertEqual(a.getNext(), b)
        self.assertEqual(a.getPrev(), None)
        self.assertEqual(b.getNext(), None)
        self.assertEqual(b.getPrev(), None)

        with self.assertRaises(Exception):
            dcll.popHead()


if __name__ == '__main__':
    unittest.main()
