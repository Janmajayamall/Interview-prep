class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        explored_set={}
        def comb(curr):
            
            if curr in explored_set:
                return explored_set[curr]
            
            if curr==target:
                return 1
        
            if curr>target:
                return 0
            
            result=0
            
            for i in nums:
                result+=comb(curr+i)
                
            explored_set[curr]=result
            return result
        
        return comb(0)
        