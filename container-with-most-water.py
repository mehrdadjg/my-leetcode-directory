""" As of 03/25/2022 09:31
    Runtime: 877 ms (beats 63.61% of python3 submissions)
    Memory: 27.5 MB (beats 59.87% of python3 submissions)
    Overall: Pretty good...
"""
class Solution:
    def maxArea(self, heights):
        biggest = 0
        
        left = 0
        right = len(heights) - 1

        while left < right:
            biggest = max(biggest, min(heights[left], heights[right]) * (right - left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return biggest

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
