""" As of 03/26/2022 18:06
    Runtime: 48 ms (beats 62.63% of python3 submissions)
    Memory: 14.3 MB (beats 11.22% of python3 submissions)
"""
from string import digits

def isBigger(log1, log2):
    v1 = ' '.join(log1.split(' ')[1:])
    v2 = ' '.join(log2.split(' ')[1:])

    return v1 > v2 if v1 != v2 else log1.split(' ')[0] > log2.split(' ')[0]

def bubble_up(arr, last_index, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left <= last_index and isBigger(arr[left], arr[smallest]):
        smallest = left
    
    if right <= last_index and isBigger(arr[right], arr[smallest]):
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        bubble_up(arr, last_index, smallest)

def heapify(arr, last_index):
    for i in range((last_index + 1)//2 - 1, -1, -1):
        bubble_up(arr, last_index, i)

def sort(arr, last_index):
    heapify(arr, last_index)

    for i in range(last_index, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        bubble_up(arr, i - 1, 0)

class Solution:
    def isDigitLog(self, log):
        if log.split(' ')[1][0] in digits:
            return True
        
        return False

    def reorderLogFiles(self, logs):
        n = len(logs)
        
        seen = 0
        i = 0
        while seen < n:
            log = logs[i]
            if self.isDigitLog(log):
                logs.remove(log)
                logs.append(log)
            else:
                i += 1
            
            seen += 1
        
        sort(logs, i - 1)
        
        return logs

s = Solution()
# print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
# print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))

print(s.reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"]))