"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root==None:
            return None
        
        class Queue():
            
            def __init__(self):
                self.q = []
            
            def push(self, x):
                self.q.append(x)
            
            def pop(self):
                temp = self.q[0]
                self.q=self.q[1:]
                return temp
            
            def isempty(self):
                return len(self.q)==0
        
        
        q1=Queue()
        q2=Queue()
        
        q1.push(root)
        
        while( not q1.isempty() ):
            last_ref = None
            while ( not q1.isempty() ):
                
                temp = q1.pop()
                temp.next=last_ref
                
                last_ref = temp
                
                if temp.right!=None:
                    q2.push(temp.right)
                
                if temp.left!=None:
                    q2.push(temp.left)
            
            q1.q = q2.q
            q2.q = []
        
        return root
                
            
        