""" As of 09/24/2020 16:51
    Runtime: 2884 ms (beats 55.95% of python3 submissions)
    Memory: 14.1 MB (beats 44.05% of python3 submissions)
    Note to Future Self: Avoid python loops as much as possible
    if you're in a rush. List comprehension's the way to go.
"""
class Solution:
    def printPretty(self, res):
        for i in range(len(res)):
            for j in range(i, len(res)):
                print("{:>2}".format(res[i][j]), end=", ")

            print()
            print("    " * (i+1), end="")
        print()

    def minimumMoves(self, arr):
        n = len(arr)
        res = [[n for i in range(n)] for i in range(n)]

        for x in range(n-1, -1, -1):
            for i in range(x+1):
                j = i + n - 1 - x

                if i == j:
                    res[i][j] = 1
                elif i == j - 1:
                    res[i][j] = {True: 1, False: 2}[arr[i] == arr[j]]
                else:
                    res[i][j] = min([res[i][k] + res[k+1][j]
                                     for k in range(i, j)])

                    if arr[i] == arr[j]:
                        res[i][j] = min(res[i][j], res[i+1][j-1])

        # self.printPretty(res)
        return res[0][n-1]


s = Solution()
print(s.minimumMoves([1, 14, 18, 20, 14]))
