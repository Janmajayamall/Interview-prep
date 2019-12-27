class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        
        dp = []
        
        for i in nums:
            dp.append(1)
        
        for i in range(len(nums)):
            j = 0
            while(j<i):
                if nums[j]<nums[i]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                j+=1
        
        return max(dp)
                        
        
        