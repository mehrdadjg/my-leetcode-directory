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
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]

class Solution:
    def minRemoveToMakeValid(self, inp):
        to_be_removed_index = []

        stack = Stack()

        for i in range(len(inp)):
            ch = inp[i]
            if ch == '(':
                stack.push((ch, i))
            elif ch == ')':
                if stack.isEmpty() or stack.peek()[0] != '(':
                    to_be_removed_index.append(i)
                else:
                    stack.pop()
        
        tmp = []
        while stack.isEmpty() == False:
            (ch, i) = stack.pop()
            tmp.append(i)
        
        for item in tmp[::-1]:
            to_be_removed_index.append(item)
        
        for i in to_be_removed_index[::-1]:
            inp = inp[0:i] + inp[i+1:]
        
        return inp

s = Solution()

print(s.minRemoveToMakeValid("))(("))