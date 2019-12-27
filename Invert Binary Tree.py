# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def invert(node):
            
            if node==None:
                return
            
            
            invert(node.left)
            invert(node.right)
            
            temp=node.left
            node.left=node.right
            node.right=temp
            
            return
    
        invert(root)
        return root