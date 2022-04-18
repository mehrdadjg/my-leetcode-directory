class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return '{}'.format(self.value)
    
    def __hash__(self):
        return hash(self.value)

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0

class Solution:
    def pathFromRoot(self, root, p):
        if root == p:
            return [root]
        
        stack = Stack()
        
        parent = {}
        current = root

        while current != None:
            if current.right != None:
                parent[current.right] = current
                stack.push(current.right)

            if current.left != None:
                parent[current.left] = current
                stack.push(current.left)

            if current.left == p or current.right == p:
                break

            current = stack.pop()
        
        result = [p]
        current = p
        while current != root:
            result = [parent[current]] + result

            current = parent[current]
        
        return result

    def lowestCommonAncestor(self, root, p, q):
        pathP = self.pathFromRoot(root, p)
        pathQ = self.pathFromRoot(root, q)

        if len(pathP) == 1 or len(pathQ) == 1:
            return root

        i = 1
        while i < min(len(pathP), len(pathQ)):
            if pathP[i] != pathQ[i]:
                return pathP[i-1]

            i += 1

        if i == len(pathP):
            return p
        else:
            return q

p = Node(5, Node(6), Node(2, Node(7), Node(4)))
q = Node(1, Node(0), Node(8))

tree = Node(3, p, q)

s = Solution()
print(s.lowestCommonAncestor(tree, p, q))
# print(s.pathFromRoot(tree, q))