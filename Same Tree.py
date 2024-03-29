# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def check(t1, t2):
            
            if t1==None and t2==None:
                return True
            
            if t1==None or t2==None:
                return False
            
            if t1.val!=t2.val:
                return False
            
            left = check(t1.left, t2.left)
            right = check(t1.right, t2.right)
            
            return (left and right)
        
        return check(p, q)