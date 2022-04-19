# Definition for singly-linked list.
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        
        temp = head.next
        rest = self.reverseList(head.next)

        temp.next = head
        head.next = None
        head = rest

        return head

s = Solution()
a = s.reverseList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
print(a.next.next.next.next.next)