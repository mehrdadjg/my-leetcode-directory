""" As of 03/27/2022 12:30
    Runtime: 48 ms (beats 43.68% of python3 submissions)
    Memory: 13.9 MB (beats 29.43% of python3 submissions)
"""
class Solution:
    def __init__(self):
        self.map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

    def isOpening(self, s):
        if s in ['(', '[', '{']:
            return True
        return False
    
    def openingPair(self, s):
        return self.map[s]

    def isValid(self, s):
        stack = []

        for ch in s:
            if self.isOpening(ch):
                stack.append(ch)
            elif len(stack) == 0:
                return False
            else:
                last = stack[-1]
                if last != self.openingPair(ch):
                    return False
                else:
                    stack.pop()
        
        return stack == []

s = Solution()
print(s.isValid('{()[{[]}]}[()][]'))