""" As of 09/22/2020 16:14 MST
    Runtime: 408 ms (beats 45.19% of python3 submissions)
    Memory: 37.1 MB (beats 5.01% of python3 submissions)
    Overall: Ouch for the memory...
"""
from Library.SkipTrie import SkipTrie


class WordDictionary:
    def __init__(self):
        self.st = SkipTrie()

    def addWord(self, word):
        self.st.addWord(word)

    def search(self, word):
        return self.st.lookUp(word)


s = WordDictionary()
s.addWord("bad")
s.addWord("dad")
s.addWord("mad")

print(s.search("pad"))
print(s.search("bad"))
print(s.search(".ad"))
print(s.search("b.."))
