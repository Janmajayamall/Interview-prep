# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head_list = []
        for i in lists:
            head_list.append(i)
        
        newHead = None
        head_ = newHead
        
        while True:
            min_v = 10000000000000000000000000000000000
            mark = None
            for index in range(len(head_list)):
                
                if head_list[index]==None:
                    continue
    
                if head_list[index].val<min_v:
                    min_v = head_list[index].val
                    mark = index
        
            if mark!=None:
                
                if newHead==None:
                    newHead=ListNode(head_list[mark].val)
                    head_=newHead
                else:
                    temp = ListNode(head_list[mark].val)
                    newHead.next = temp
                    newHead = newHead.next
                head_list[mark]=head_list[mark].next
            else:
                break
        
        return head_
        
            
            