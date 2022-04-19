class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
    
    def setParent(self, node):
        self.parent = node
    
    def __eq__(self, other):
        if other == None:
            return False

        return self.value == other.value

class Solution:
    def __init__(self):
        self.islands = {}
        self.islandCount = 0
    
    def addIsland(self, row, col):
        self.islands[(row, col)] = Node((row, col))
        self.islandCount += 1
    
    def __getIslandSet__(self, row, col):
        current = self.islands[(row, col)]

        while current.parent != None:
            current = current.parent
        
        tmp = self.islands[(row, col)]
        while tmp.parent != None:
            x = tmp.parent
            tmp.parent = current

            tmp = x
        
        return current
    
    def mergeIslands(self, row1, col1, row2, col2):
        set1 = self.__getIslandSet__(row1, col1)
        set2 = self.__getIslandSet__(row2, col2)

        if set1 != set2:
            set1.setParent(set2)
            self.islandCount -= 1
    
    def getTotalIslandCount(self):
        return self.islandCount
    
    def __north__(self, row, col):
        if row == 0:
            return False
        
        return (row - 1, col)
    
    def __west__(self, row, col):
        if col == 0:
            return False
        
        return (row, col - 1)
    
    def numIslands(self, grid):
        totalRows = len(grid)
        totalColumns = len(grid[0])

        for row in range(totalRows):
            for col in range(totalColumns):
                if grid[row][col] == '1':
                    self.addIsland(row, col)

                    if self.__north__(row, col) != False:
                        (nRow, nCol) = self.__north__(row, col)
                        if grid[nRow][nCol] == '1':
                            self.mergeIslands(row, col, nRow, nCol)
                    
                    if self.__west__(row, col) != False:
                        (wRow, wCol) = self.__west__(row, col)
                        if grid[wRow][wCol] == '1':
                            self.mergeIslands(row, col, wRow, wCol)
        
        return self.getTotalIslandCount()

s = Solution()

print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))