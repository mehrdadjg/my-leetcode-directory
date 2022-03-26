""" As of 03/23/2022 15:35
    Runtime: 71 ms (beats 7.71% of python3 submissions)
    Memory: 14 MB (beats 6.19% of python3 submissions)
    Overall: We're doing it in one pass!
"""
class Solution:
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None
        
        nodes = [None] * 30
        length = 0

        current = head
        while current != None:
            nodes[length] = current
            length += 1

            current = current.next;
        
        d_index = length - n
        if d_index > 0:
            nodes[d_index - 1].next = nodes[d_index + 1]
        else:
            head = head.next

        return head


l = ListNode(1, ListNode(2))

s = Solution()
print(s.removeNthFromEnd(l, 1).next)