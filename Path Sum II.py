# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        final_list=[]
        
        def findSum(node, value, curr):
            
            if node == None:
                return 
            
            value+=node.val
            curr.append(node.val)
            
            if sum==value:
                if node.left==None and node.right==None:
                        final_list.append(curr[::])
                
            findSum(node.left, value, curr)
            findSum(node.right, value, curr)
            
            value-=node.val
            curr.pop()
            
            return 
        
        findSum(root, 0, [])
        
        return final_list
            
            
            
            
            
                    
                
            