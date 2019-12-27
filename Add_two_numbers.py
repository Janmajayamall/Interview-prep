# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        head_ = None
        co = 0
        while (l1!=None or l2!=None):
            
            sum_val = 0
            
            sum_val+=co
            co=0
            
            if l1!=None:
                sum_val+=l1.val
                l1=l1.next
                
            if l2!=None:
                sum_val+=l2.val
                l2=l2.next
                
            if sum_val>=10:
                co=1
                sum_val = sum_val%10
            
            if head==None:
                temp = ListNode(sum_val)
                head = temp
                head_ = head
            else:
                temp = ListNode(sum_val)
                head.next = temp
                head = temp
            
        if co!=0:
            temp = ListNode(co)
            head.next = temp
            head = temp
        
        return head_
        
        