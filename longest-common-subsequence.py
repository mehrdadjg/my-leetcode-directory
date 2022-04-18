""" As of 04/17/2022 19:03
    Runtime: 441 ms (beats 79.77% of python3 submissions)
    Memory: 22.7 MB (beats 58.56% of python3 submissions)
"""
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        l1 = len(text1)
        l2 = len(text2)

        prefix = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]

        for i in range(l1):
            for j in range(l2):
                if text1[i] == text2[j]:
                    prefix[i+1][j+1] = prefix[i][j] + 1
                else:
                    prefix[i+1][j+1] = max(prefix[i][j+1], prefix[i+1][j])
        
        # result = ''
        # i = l1
        # j = l2

        # while i > 0 and j > 0:
        #     if text1[i-1] == text2[j-1]:
        #         result = text1[i-1] + result
        #         i -= 1
        #         j -= 1
        #     else:
        #         if prefix[i][j-1] > prefix[i-1][j]:
        #             j -= 1
        #         else:
        #             i -= 1
        
        # print(result)

        return prefix[l1][l2]

s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))