import math

class CustomMinMaxHeap:
    def __init__(self, size, initial):
        if len(initial) < size:
            initial.append(-1000000)
        self.heap = [i for i in initial]
        self.size = size

        for i in range(size // 2 - 1, -1, -1):
            self.__heapify__(i)
    
    def __repr__(self):
        return str(self.heap)
    
    def __heapify__(self, i):
        if self.__isMinLayer__(i):
            self.__trickle_down_min__(i)
        else:
            self.__trickle_down_max__(i)
    
    def __isMinLayer__(self, i):
        return math.floor(math.log2(i+1)) % 2 == 0
    
    def __trickle_down_min__(self, i):
        if self.__has_child__(i):
            children_and_granchildren = self.__get_children_n_grandchildren__(i)
            minimum_index = children_and_granchildren[0]
            for offspring_index in children_and_granchildren[1:]:
                if self.heap[offspring_index] < self.heap[minimum_index]:
                    minimum_index = offspring_index
            
            # minimum is a grandchild
            if self.__isMinLayer__(minimum_index):
                if self.heap[minimum_index] < self.heap[i]:
                    self.heap[minimum_index], self.heap[i] = self.heap[i], self.heap[minimum_index]
                    
                    parent_index = self.__get_parent_index__(minimum_index)
                    if self.heap[minimum_index] > self.heap[parent_index]:
                        self.heap[minimum_index], self.heap[parent_index] = self.heap[parent_index], self.heap[minimum_index]
                    
                    self.__trickle_down_min__(minimum_index)
            # minimum is a child
            else:
                if self.heap[minimum_index] < self.heap[i]:
                   self.heap[minimum_index], self.heap[i] = self.heap[i], self.heap[minimum_index]
    
    def __trickle_down_max__(self, i):
        if self.__has_child__(i):
            children_and_granchildren = self.__get_children_n_grandchildren__(i)
            maximum_index = children_and_granchildren[0]
            for offspring_index in children_and_granchildren[1:]:
                if self.heap[offspring_index] > self.heap[maximum_index]:
                    maximum_index = offspring_index
            
            # maximum is a grandchild
            if self.__isMinLayer__(maximum_index) == False:
                if self.heap[maximum_index] > self.heap[i]:
                    self.heap[maximum_index], self.heap[i] = self.heap[i], self.heap[maximum_index]
                    
                    parent_index = self.__get_parent_index__(maximum_index)
                    if self.heap[maximum_index] < self.heap[parent_index]:
                        self.heap[maximum_index], self.heap[parent_index] = self.heap[parent_index], self.heap[maximum_index]
                    
                    self.__trickle_down_max__(maximum_index)
            # maximum is a child
            else:
                if self.heap[maximum_index] > self.heap[i]:
                   self.heap[maximum_index], self.heap[i] = self.heap[i], self.heap[maximum_index]
    
    def __has_child__(self, i):
        return 2 * i + 1 < self.size
    
    def __get_children_n_grandchildren__(self, i):
        result = []
        for candidate in [2 * i + 1, 2 * i + 2, 2 * (2 * i + 1) + 1, 2 * (2 * i + 1) + 2, 2 * (2 * i + 2) + 1, 2 * (2 * i + 2) + 2]:
            if candidate < self.size:
                result.append(candidate)
        
        return result
    
    def __get_parent_index__(self, i):
        if i == 0:
            return None

        return (i - 1) // 2
    
    def maintain(self, num):
        if num < self.getMinimum():
            return
        
        self.heap[0] = num
        self.__heapify__(0)
    
    def getMinimum(self):
        return self.heap[0]

class KthLargest:
    def __init__(self, k, nums):
        self.heap = CustomMinMaxHeap(k, nums[:k])

        for num in nums[k:]:
            self.heap.maintain(num)

    def add(self, num):
        self.heap.maintain(num)

        return self.heap.getMinimum()


s = KthLargest(1, [])
print(s.add(-3))
print(s.add(-2))
print(s.add(-4))
print(s.add(0))
print(s.add(4))