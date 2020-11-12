""" As of 11/11/2020 19:18 MST
    Runtime: 60 ms (beats 61.68% of python3 submissions)
    Memory: 14.2 MB (beats 7.03% of python3 submissions)
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s


        totalDistance = 2*(numRows)-2
        currentDistance = 0
        res = ""
        for row in range(numRows):
            alternate = not (row == numRows-1)
            index = row
            while index < len(s):
                res += s[index]

                if alternate:
                    index += (totalDistance - currentDistance)
                else:
                    index += currentDistance

                if row == 0:
                    alternate = True
                elif row == numRows - 1:
                    alternate = False
                else:
                    alternate = not alternate

            currentDistance += 2
        
        return res