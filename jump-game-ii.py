""" As of 03/23/2022 11:37
    Runtime: 1465 ms (beats 33.38% of python3 submissions)
    Memory: 14.9 MB (beats 91.54% of python3 submissions)
    Overall: Not bad...
"""
class Solution:
    def jump(self, nums):
        n = len(nums)

        if n in [1, 2]:
            return n - 1
        
        result = [0] * n
        result[-2] = 1

        for i in range(-3, -(n+1), -1):
            jump_length = nums[i]
            limit = i+1+jump_length
            jump_nums_range = result[i+1:] if limit >= 0 else result[i+1:limit]
            
            result[i] = 1 + min(jump_nums_range) if jump_nums_range != [] else n+1

        return result[0]