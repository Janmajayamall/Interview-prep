class Solution:
    
    # remember that in this case,
    #     I am trying to find the maximum amount we can rob if we rob the first one or
    #     the last one. 
    #     By forming different lists, one with first house and second without first house,
    #     we are trying to avoid the best case of when both of them are robbed in order to
    #     maximise the amount
    
    def rob(self, nums: List[int]) -> int:

        
        def robCalc(vals):
            
            if vals==None or len(vals)==0:
                return 0
    
            if len(vals)==1:
                return vals[0]

            if len(vals)==2:
                return max(vals)
        
            dp = [vals[0], max(vals[0], vals[1])] 
            
            for i in range(2, len(vals)):
                
                dp.append(max(dp[-1], dp[-2]+vals[i]))
            
            return dp[-1]
    
            
        
        if nums==None or len(nums)==0:
            return 0
    
        if len(nums)==1:
            return nums[0]
                
        if len(nums)==2:
            return max(nums)
        
        return max(robCalc(nums[1:]), robCalc(nums[:-1]))
        