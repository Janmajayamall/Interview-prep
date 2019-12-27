
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def permute (index, num_list, current, explored):
            
            for i in range(index, len(num_list)):
                
                current.append(num_list[i])
                
                explored.append(current[::])
                permute(i+1, num_list, current, explored)
                
                current.pop()
            
        explored = [[]]
        
        permute(0, nums, [], explored)
        
        return explored