""" As of 03/25/2022 12:14
    Runtime: 138 ms (beats 47.20% of python3 submissions)
    Memory: 14.1 MB (beats 73.71% of python3 submissions)
    Overall: Not bad...
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        middle = (((m + n + 2) // 2) - 1,) if (m + n) % 2 == 1 else (((m + n) // 2) - 1, ((m + n + 2) // 2) - 1)

        count = 0
        i = 0
        j = 0

        p = nums1[i] if i < m else None
        q = nums2[j] if j < n else None

        result = 0

        while count <= middle[-1]:
            if count in middle:
                if p != None and q != None:
                    result += min(p, q)
                elif p == None:
                    result += q
                else:
                    result += p
            
            if p != None and q != None:
                if p < q:
                    i += 1
                    p = nums1[i] if i < m else None
                else:
                    j += 1
                    q = nums2[j] if j < n else None
            elif p == None:
                j += 1
                q = nums2[j] if j < n else None
            else:
                i += 1
                p = nums1[i] if i < m else None

            count += 1

        return result / len(middle)

s = Solution()
print(s.findMedianSortedArrays([], [2, 7]))
print(s.findMedianSortedArrays([1,2, 7], [3,4]))
