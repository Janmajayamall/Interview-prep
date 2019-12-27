# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        if head == None:
            return None

        def create(vals):
            
            if len(vals)==0:
                return None
            
            mid = len(vals)//2
            node = TreeNode(vals[mid])
            
            node.left = create(vals[:mid])
            node.right = create(vals[mid+1:])
            
            return node
        
        values = []
        
        while (head!=None):
            
            values.append(head.val)
            head=head.next
    
        
        
        return create(values)
            
        