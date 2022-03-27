""" As of 03/25/2022 15:16
    Runtime: 54 ms (beats 45.49% of python3 submissions)
    Memory: 14.4 MB (beats 16.28% of python3 submissions)
"""
class Solution:
    def __init__(self):
        self.memory = {
            1: ['()']
        }

    def generateParenthesis(self, n):
        if n in self.memory:
            return self.memory[n]
        elif n == 0:
            return ['']
        
        result1 = ['()' + x for x in self.generateParenthesis(n - 1)]
        result2 = ['(' + x + ')' + y for i in range(n-1, 0, -1) for x in self.generateParenthesis(n - i) for y in self.generateParenthesis(i - 1)]

        self.memory[n] = result1 + result2
        return result1 + result2

s = Solution()
print(s.generateParenthesis(4))