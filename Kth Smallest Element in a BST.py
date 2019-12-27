# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root1, k1):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        def inorder(root, k, count):
            
            if root==None:
                return count, None
            
            left = inorder(root.left, k, count)
            if left[1]!=None:
                return left
            
            count=left[0]+1
            if count==k:
                return count, root.val
            
            right = inorder(root.right, k, count)
            return right
        
        return inorder(root1, k1, 0)[1]