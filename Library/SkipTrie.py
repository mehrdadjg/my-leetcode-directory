import unittest


class Node:
    def __init__(self, value=None):
        self.value = value

        self.isLeaf = False
        self.parent = None
        self.children = {}

    def __repr__(self):
        return '{}, {}'.format(self.value, self.isLeaf)

    def findChild(self, char):
        if char not in self.children:
            return None
        else:
            return self.children[char]

    def addChild(self, char, child):
        if char in self.children:
            raise ValueError('Child ({}) already exists.'.format(char))

        self.children[char] = child
        child.parent = self

        return child

    def setLeaf(self, isLeaf=True):
        self.isLeaf = isLeaf


class SkipTrie:
    def __init__(self):
        self.storage = Node()

    def __repr__(self):
        return self.storage.__repr__()

    def addWord(self, word):
        currentNode = self.storage
        for i in range(len(word)):
            char = word[i]

            child = currentNode.findChild(char)
            if child != None:
                currentNode = child
            else:
                newNode = Node(word[:i+1])
                currentNode.addChild(char, newNode)
                currentNode = newNode

        currentNode.setLeaf()

    def lookUpHelper(self, word_pattern, node):
        if word_pattern == '' and node != None:
            return node.isLeaf
        elif word_pattern != '' and node == None:
            return False
        elif word_pattern == '' and node == None:
            return True
        else:
            currentNode = node
            for i in range(len(word_pattern)):
                char = word_pattern[i]

                if char != '.':
                    if char not in currentNode.children:
                        return False

                    childNode = currentNode.children[char]
                    currentNode = childNode
                else:
                    for child in currentNode.children.values():
                        if self.lookUpHelper(word_pattern[i+1:], child):
                            return True
                    return False

            return currentNode.isLeaf

    def lookUp(self, word_pattern):
        return self.lookUpHelper(word_pattern, self.storage)


class TestDoublyConnectedLinkedList(unittest.TestCase):
    def test_1(self):
        st = SkipTrie()
        self.assertFalse(st.lookUp(''))
        st.addWord('')
        self.assertTrue(st.lookUp(''))
        st.addWord('a')
        st.addWord('ab')
        st.addWord('abc')
        st.addWord('a')
        self.assertTrue(st.lookUp('a'))
        self.assertTrue(st.lookUp('a.'))
        self.assertTrue(st.lookUp('a..'))
        self.assertTrue(st.lookUp('.bc'))
        self.assertTrue(st.lookUp('a.c'))
        self.assertTrue(st.lookUp('.b.'))
        self.assertFalse(st.lookUp('....'))
        self.assertTrue(st.lookUp('...'))


if __name__ == '__main__':
    unittest.main()
