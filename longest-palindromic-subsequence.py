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

        return prefix[l1][l2]

    def longestPalindromeSubseq(self, text):
        reverse = text[::-1]
        return self.longestCommonSubsequence(text, reverse)