class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sumvalue = sum(nums)//k
        
        def permute(currSum, nb, vals):
            
            if nb==k and currSum==0:
                return True
            
            if len(vals)==0:
                return False
            
            for i in range(len(vals)):
                
                currSum+=vals[i]
                temp = vals[:i]+vals[i+1:]
                
                if currSum>sumvalue:
                    currSum-=vals[i]
                    continue
                
                result=False
                
                if currSum == sumvalue:
                    result = permute(0, nb+1, temp)
                else:
                    result = permute(currSum, nb, temp)
                    
                if result:
                    return True
                
                currSum-=vals[i]
            
            return False
        
        return permute(0, 0, nums)
                
            
        
        
        
        