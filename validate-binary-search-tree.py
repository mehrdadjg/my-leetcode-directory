""" As of 09/24/2020 09:33 MST
    Runtime: 72 ms (beats 15.03% of python3 submissions)
    Memory: 16.6 MB (beats 9.65% of python3 submissions)
    Overall: Turns out yield and recursion aren't the most
    efficient combo, they're fun to use though.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrder(self, node):
        if node == None:
            return

        for val in self.inOrder(node.left):
            yield val

        yield node.val

        for val in self.inOrder(node.right):
            yield val

    def isValidBST(self, root):
        previous = None
        for val in self.inOrder(root):
            if previous != None and previous >= val:
                return False

            previous = val

        return True


tree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))

s = Solution()
print(s.isValidBST(tree))
