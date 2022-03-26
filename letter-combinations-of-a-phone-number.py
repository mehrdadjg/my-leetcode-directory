""" As of 03/25/2022 15:16
    Runtime: 31 ms (beats 88.83% of python3 submissions)
    Memory: 13.9 MB (beats 82.80% of python3 submissions)
    Overall: good...
"""
class Solution:
    def __init__(self):
        self.map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
    
    def letterCombinations(self, digits):
        n = len(digits)

        if digits == "":
            return []
        elif n == 1:
            return self.map[digits]
        elif n == 2:
            return [x + y for x in self.map[digits[0]] for y in self.map[digits[1]]]
        elif n == 3:
            return [x + y + z for x in self.map[digits[0]] for y in self.map[digits[1]] for z in self.map[digits[2]]]
        elif n == 4:
            return [x + y + z + a for x in self.map[digits[0]] for y in self.map[digits[1]] for z in self.map[digits[2]] for a in self.map[digits[3]]]
        
        return result

s = Solution()
print(s.letterCombinations('4444'))