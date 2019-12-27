class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        final_list=[]
        
        def perm(num_list, current, explored):
            
            if len(num_list)==0:
                final_list.append(current[::])
            
            for i in range(len(num_list)):
                
                current.append(num_list[i])
                if current not in explored:
                    temp = num_list[:i]+num_list[i+1:]
                    explored.append(current[::])
                    perm(temp, current, explored)

                
                current.pop()
        
        perm(nums, [], [])
            
        return final_list
                
                    