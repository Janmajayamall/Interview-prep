# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def build(ino, pre):
            if len(pre)==0 :
                return
            
            root = pre[0]
            index = None
            for i in range(len(ino)):
                if ino[i]==root:
                    index=i
            
            node = TreeNode(root)
            node.left = build(ino[:index], pre[1:index+1])
            node.right = build(ino[index+1:], pre[index+1:])
            
            return node 
        
        return build(inorder, preorder)
        