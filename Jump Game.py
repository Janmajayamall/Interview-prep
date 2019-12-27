class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
            
        if len(nums)==0:
            return False
        
        def jump(currVal, vals, jumps):
            
            if currVal==len(vals)-1:
                return True
        
            if currVal>=len(vals):
                return False    
            
        
            for i in range(1, jumps+1):
                
            
                if jump(currVal+i, vals, vals[currVal+i]):
                    return True
               
            return False 
        
        return jump(0, nums, nums[0])