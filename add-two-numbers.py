""" As of 03/22/2022 23:10 MST
    Runtime: 133 ms (beats 14.05% of python3 submissions)
    Memory: 14 MB (beats 52.11% of python3 submissions)
    Overall: Not impressive buddy...
"""
class Solution:
    def toDecimal(self, l):
        if l == None:
            return 0
        elif l.next == None:
            return l.val
        else:
            other = self.toDecimal(l.next)
            return other * 10 + l.val
    
    def toList(self, d):
        if d < 10:
            return ListNode(d)
        
        result = ListNode(d % 10)
        last = result
        d = d // 10

        while d > 0:
            last.next = ListNode(d % 10)
            last = last.next
            d = d // 10
        
        return result


    def addTwoNumbers(self, l1, l2):
        sum = self.toDecimal(l1) + self.toDecimal(l2)
        return self.toList(sum)