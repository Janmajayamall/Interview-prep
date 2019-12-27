"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head==None:
            return None
        
        hash_set = {}
        curr = head
        while curr!=None:
            
            temp = Node(curr.val, None, None)
            hash_set[curr]=temp
            curr=curr.next
        
        curr=head
        
        while curr!=None:
            
            if curr.next !=None:
                hash_set[curr].next = hash_set[curr.next]
            if curr.random!=None:
                hash_set[curr].random = hash_set[curr.random]
            curr=curr.next
            
        
        return hash_set[head]
            
            
            
            
            