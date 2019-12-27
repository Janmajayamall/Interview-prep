# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def valid(rootNode, leftRange, rightRange):
            
            if rootNode==None:
                return True
            
            if rootNode.val<rightRange and rootNode.val>leftRange:
                
                left = valid(rootNode.left, leftRange, rootNode.val)
                right = valid(rootNode.right, rootNode.val, rightRange)
                
                return left and right
                
            else:
                return False
        
        return valid(root, -10000000000000000000000,10000000000000000000000 )