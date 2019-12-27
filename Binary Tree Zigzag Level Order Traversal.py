# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root==None:
            return []
        
        class Stack():
            
            def __init__(self):
                self.stack = []
            
            def push(self, x):
                self.stack.append(x)
            
            def pop(self):
                if len(self.stack)==0:
                    return None
                pop = self.stack[-1]
                self.stack=self.stack[:-1]
                return pop
            
            def isempty(self):
                return len(self.stack)==0
        
        s1 = Stack()
        s2 = Stack()
        
        s1.push(root)
        
        rightLeft=False
        
        final_list=[]
        
        while(not s1.isempty()):
            temp = []
            while(not s1.isempty()):
                
                node = s1.pop()
                temp.append(node.val)
                
                if rightLeft:
                    if node.right!=None:
                        s2.push(node.right)
                    if node.left!=None:
                        s2.push(node.left)
                    
                else:
                    if node.left!=None:
                        s2.push(node.left)
                    if node.right!=None:
                        s2.push(node.right)
                
            
            s1.stack=s2.stack
            s2.stack=[]
            final_list.append(temp)
            rightLeft=not rightLeft
            
        return final_list
            
                
                
                
                
                
                
        