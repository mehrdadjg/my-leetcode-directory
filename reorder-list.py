# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        if self.next == None:
            return '{}'.format(self.val)

        return '{} -> {}'.format(self.val, self.next.__repr__())

class Solution:
    def reorderList(self, head):
        nodes = []
        temp = head
        while temp != None:
            nodes.append(temp)
            temp = temp.next
        count = len(nodes)

        if count <= 2:
            return
        
        first = nodes[0]
        last = nodes[-1]
        before_last = nodes[-2]
        for i in range(count // 2 if count % 2 == 1 else ((count // 2) - 1)):
            last.next = first.next
            before_last.next = None
            first.next = last

            first = last.next
            last = before_last
            before_last = nodes[-2-i-1]



s = Solution()
linkedlist = Node(1, Node(2, Node(3, Node(4))))
print(linkedlist)
s.reorderList(linkedlist)
print(linkedlist)