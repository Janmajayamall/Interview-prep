class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=[]
        self.s2=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.s1)==0:
            return None
        
        while(len(self.s1)!=1):
            temp = self.s1[-1]
            self.s2.append(temp)
            self.s1=self.s1[:-1]
        pop = self.s1[0]
        self.s1 = []
        while(len(self.s2)!=0):
            temp = self.s2[-1]
            self.s1.append(temp)
            self.s2=self.s2[:-1]
        return pop
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.s1)==0:
            return None
        else:
            return self.s1[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()