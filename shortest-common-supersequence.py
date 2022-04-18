""" As of 04/17/2022 22:44
    Runtime: 446 ms (beats 90.24% of python3 submissions)
    Memory: 22.7 MB (beats 72.80%  of python3 submissions)
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
        
        result = []
        i = l1
        j = l2

        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                result = [(i-1, j-1)] + result
                i -= 1
                j -= 1
            else:
                if prefix[i][j-1] > prefix[i-1][j]:
                    j -= 1
                else:
                    i -= 1

        return result

    def shortestCommonSupersequence(self, text1, text2):
        lcs = self.longestCommonSubsequence(text1, text2)

        if len(lcs) == 0:
            return text1 + text2
        
        result = text1[:lcs[0][0]] + text2[:lcs[0][1]]

        for current_index in range(len(lcs)):
            (i, j) = lcs[current_index]
            result = result + text1[i]
            if current_index != len(lcs) - 1:
                (i_2, j_2) = lcs[current_index + 1]
                result  = result + text1[i+1:i_2] + text2[j+1:j_2]
            else:
                result  = result + text1[i+1:] + text2[j+1:]
        
        return result

s = Solution()
print(s.shortestCommonSupersequence('abac', 'cab'))
print(s.shortestCommonSupersequence('aaaaaaaa', 'aaaaaaaa'))