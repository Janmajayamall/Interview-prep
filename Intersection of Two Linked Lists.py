# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if headA==None or headB==None:
            return None
        
        headA_ref = headA
        headB_ref = headB
        
        headA_prev = True
        headB_prev = True
        
        lA = None
        lB = None
        
        while lA==None or lB==None:
            
            if headA_ref!=None and headA_ref.next==None:
                lA = headA_ref
            
            if headB_ref!=None and headB_ref.next==None:
                lB = headB_ref
            
            if headA_ref:
                headA_ref=headA_ref.next
            if headB_ref:
                headB_ref=headB_ref.next
        
        print(lA.val, lB.val)
        if lA!=lB:
            return None
            
        headA_ref = headA
        headB_ref = headB
        
        while True:
            
            if headA_ref==None:
                
                if headA_prev:
                    headA_ref = headB
                    headA_prev = False
                else:
                    headA_ref = headA
                    headA_prev = True
                
                continue
                    
            if headB_ref == None:
                
                if headB_prev:
                    headB_ref = headA
                    headB_prev = False
                else:
                    headB_ref = headB
                    headB_prev = True
                
                continue
            
            if headA_ref==headB_ref:
                print(headA_ref.val)
                break
        
            headA_ref=headA_ref.next
            headB_ref=headB_ref.next
            
            
        return headA_ref
            
            
            
            
                
            
            
            
            