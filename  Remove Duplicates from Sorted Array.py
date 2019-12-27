class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        
        i = 0
        j = 0
        
        while(j<len(nums) and i<len(nums)):
            
            while(j<len(nums) and (nums[j]==nums[i])):
                j+=1
            
            if j<len(nums):                
                nums[i+1]=nums[j]
                
            i+=1

        while(len(nums)!=i):

            nums.pop()