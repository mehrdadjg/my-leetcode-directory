""" As of 03/23/2022 15:35
    Runtime: 76 ms (beats 74.46% of python3 submissions)
    Memory: 14.1 MB (beats 57.94% of python3 submissions)
    Overall: Pretty good...
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0
        
        longest = 1
        p = 0
        q = 0

        window = s[0]

        while True:
            while q + 1 < n and s[q + 1] not in window:
                q += 1
                window += s[q]
            
            longest = max(longest, len(window))

            if q == n - 1:
                break
            
            while len(window) > 0 and s[q + 1] in window:
                window = window[1:]
                p += 1
            
            if window == '' and p + 1 < n:
                q = p
                window = s[p]
            elif window == '':
                break

        return longest
