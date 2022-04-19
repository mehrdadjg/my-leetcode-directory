# Definition for singly-linked list.
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode
    
    def __repr__(self):
        if self.next == None:
            return '{}'.format(self.value)
        else:
            return '{} -> {}'.format(self.value, self.next.__repr__())

class Solution:
    def __reverseList__(self, head):
        if head == None or head.next == None:
            return head
        
        temp = head.next
        rest = self.__reverseList__(head.next)

        temp.next = head
        head.next = None
        head = rest

        return head

    def reverseBetween(self, head, left, right):
        current_node = head
        current_position = 1
        before = None
        first = None
        last = None
        after = None

        while current_node != None:
            if current_position == left - 1:
                before = current_node
            if current_position == left:
                first = current_node
            if current_position == right:
                last = current_node
            if current_position == right + 1:
                after = current_node
            if current_position > right + 1:
                break

            current_node = current_node.next
            current_position += 1
        
        last.next = None
        reversed = self.__reverseList__(first)

        if before != None:
            before.next = reversed
        else:
            head = reversed
        
        first.next = after

        return head

s = Solution()
l = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(l)
r = s.reverseBetween(l, 2, 5)
print(r)