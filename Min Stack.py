class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min = min(self.stack)
        

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack)==0:
            self.min=None
        else:
            self.min = min(self.stack)
        

    def top(self) -> int:
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()