class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs=sorted(costs, key=lambda x:x[0]-x[1])
        
        a_count = 0
        total_sum=0
        print(costs)
        for person  in costs:
            
            if a_count<(len(costs)/2):
                total_sum += person[0]
                a_count+=1
            else:
                total_sum += person[1]
    
        return total_sum
