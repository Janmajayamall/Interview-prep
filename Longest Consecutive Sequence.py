class Solution(object):  # hard & tricky problem o(n)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==0 or nums==None:
            return 0
        
        sets = set()
        for i in nums:
            sets.add(i)
            
        maxv = -100000000000000000
            
        for i in sets:
            
            if i-1 in sets:
                continue
            else:
                curr = i
                count=0
                while (curr in sets):
                    count+=1
                    curr+=1
                
                if maxv<count:
                    maxv=count
        
        return maxv