class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def permute(index, num_list, current, explore):
            
            for i in range(index, len(num_list)):
                
                current.append(num_list[i])
                
                if current not in explore:
                    explore.append(current[::])
                    permute(i+1, num_list, current, explore)
                
                current.pop()
            
        explore=[[]]
        permute(0, sorted(nums), [], explore)
        
        return explore
        