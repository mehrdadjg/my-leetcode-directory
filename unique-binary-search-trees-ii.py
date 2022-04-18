""" As of 04/18/2022 10:43
    Runtime: 58 ms (beats 88.18% of python3 submissions)
    Memory: 15.5 MB (beats 82.20% of python3 submissions)
"""
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        if self.left == None and self.right == None:
            return '({}, _, _)'.format(self.value)
        elif self.left == None and self.right != None:
            r = self.right.__repr__()
            return '({}, _, {})'.format(self.value, r)
        elif self.left != None and self.right == None:
            l = self.left.__repr__()
            return '({}, {}, _)'.format(self.value, l)
        else:
            l = self.left.__repr__()
            r = self.right.__repr__()
            return '({}, {}, {})'.format(self.value, l, r)

class Solution:
    def __init__(self):
        self.memory = {
            (1, 1):[ TreeNode(1) ],
        }
    
    def generateTreesHelper(self, start, end):
        if (start, end) in self.memory:
            return self.memory[(start, end)]
        elif start == end:
            self.memory[(start, end)] = [ TreeNode(start) ]
            return self.memory[(start, end)]
        elif end < start:
            return []

        result = []
        for root in range(start, end + 1):
            left = self.generateTreesHelper(start, root - 1)
            right = self.generateTreesHelper(root + 1, end)

            if len(left) == 0:
                for r in right:
                    tree = TreeNode(root, None, r)
                    result.append(tree)
            elif len(right) == 0:
                for l in left:
                    tree = TreeNode(root, l, None)
                    result.append(tree)
            else:
                for r in right:
                    for l in left:
                        tree = TreeNode(root, l, r)
                        result.append(tree)
        
        return result

    def generateTrees(self, n):
        return self.generateTreesHelper(1, n)

s = Solution()
r = s.generateTrees(4)
print(len(r))
print(r)