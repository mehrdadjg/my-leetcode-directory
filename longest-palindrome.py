""" As of 09/27/2020 14:39 MST
    Runtime: 36 ms (beats 31.42% of python3 submissions)
    Memory: 14.2 MB (beats 5.31%  of python3 submissions)
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = {}

        for ch in s:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        total = 0
        odd_exists = False
        for freq in frequency.values():
            if freq % 2 == 0:
                total += freq
            else:
                total += freq - 1
                odd_exists = True

        return total + {True: 1, False: 0}[odd_exists]


s = Solution()
print(s.longestPalindrome("abccccdd"))
