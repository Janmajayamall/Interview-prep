# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Queue:
    
    def __init__(self):
        self.queue = []
        
    def push(self, val):
        self.queue.append(val)
        
    def pop(self):
        temp = self.queue[0]
        if len(self.queue) == 1:
            self.queue = []
        else:
            self.queue = self.queue[1:]
        return temp
        
    def is_empty(self):
        return (len(self.queue)==0)

class Solution:
    
    def __init__(self):
        self.final_list = []
        self.queue = Queue()
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        q1 = Queue()
        q2 = Queue()
        
        q1.push(root)
        final_list = []
        while (not q1.is_empty()):
            temp = []
            while (not q1.is_empty()):
                
                val = q1.pop()
                
                if val!=None:
                    temp.append(val.val)
                    
                    q2.push(val.left)
                    q2.push(val.right)
            if len(temp)>0:       
                final_list.append(temp)
            q1.queue=q2.queue
            q2.queue=[]
        return final_list
                    
                
                
                
      
   
        