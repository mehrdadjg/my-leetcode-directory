class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def findPathWithSum(tree, target):
    if tree == None:
        return (target == 0, None)
    elif tree.left == None and tree.right == None:
        return (target == tree.value, [tree.value] if target == tree.value else None)
    elif target < tree.value:
        return (False, None)
    else:
        (leftFound, leftPath) = findPathWithSum(tree.left, target - tree.value)
        if leftFound:
            if leftPath != None:
                return (True, [tree.value] + leftPath)
            else:
                return (True, [tree.value])

        (rightFound, rightPath) = findPathWithSum(tree.right, target - tree.value)
        if rightFound:
            if rightPath != None:
                return (True, [tree.value] + rightPath)
            else:
                return (True, [tree.value])
        
        return (False, None)



tree = Node(4, Node(8, Node(1, Node(7)), Node(5, None, Node(3))), Node(1, None, Node(3, Node(5, None, Node(2)))))
print(findPathWithSum(tree, 20))