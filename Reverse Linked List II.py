# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count = 0
        
        head_ = head
        start = None
        end = None
        prev = None
        start_n = None
        end_n = None
        
        while(head!=None):
            
            count+=1
            
            if count==m-1:
                start=head
            
            if count==n+1:
                end=head
                
            if count==m:
                start_n=head
            
            if count==n:
                end_n=head
            
            if count>=m and count<=n:
                temp=head.next
                head.next=prev
                prev=head
                head=temp
                continue
            
            head=head.next
        
        if start==None:
            head_ = end_n
        else:
            start.next=end_n
        start_n.next=end
        
        return head_
            
                