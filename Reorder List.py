# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if head==None or head.next==None:
            return head 
    
        headNode = head.next
        
        stack = []
        
        fast=headNode
        slow=headNode
        
        odd = False
        
        while fast!=None:
            
            stack.append(slow)
            
            if fast.next!=None:
                fast=fast.next.next
                slow=slow.next
            else:
                stack=stack[:-1]
                odd=True
                break
        
        oddMark = None
        if odd==True:
            oddMark = slow
            slow=slow.next
            oddMark.next = None

        prev = oddMark

        while(len(stack)!=0):
            
            val=stack[-1]
            stack=stack[:-1]
            
            if slow!=None:
                
                nextN = slow.next

                slow.next = val
                val.next = prev
                prev = slow

                slow = nextN
            
        head.next = prev
        return head
            
                
            
        
        
        