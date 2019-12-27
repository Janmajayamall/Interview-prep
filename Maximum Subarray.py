class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ma = -1000000000000000
        final = ma
        for i in range(len(nums)):
            
            ma = max(ma+nums[i], nums[i])
            
            if ma>final:
                final=ma
        
        return final