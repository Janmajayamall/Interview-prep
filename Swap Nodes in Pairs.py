# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head==None:
            return None
        
        if head.next==None:
            return head
        
        slow = head
        fast = head.next
        head = fast
        
        slow.next = fast.next
        fast.next = slow
        
        last_ref = slow
        if slow.next!=None:
            temp = fast
            fast = slow.next.next
            slow = temp.next.next
        else:
            return head
        
        while(fast!=None):
            
            last_ref.next = fast
            slow.next = fast.next
            fast.next = slow
            last_ref = slow

            if slow.next!=None:
                temp = fast
                fast = slow.next.next
                slow = temp.next.next
            else:
                break
        
        return head