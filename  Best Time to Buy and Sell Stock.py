class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        pro = 0
        minv = 10000000000000000000
        
        for i in prices:
            
            if i < minv:
                minv = i
            else:
                if pro<(i-minv):
                    pro = i-minv
        
        return pro
                
            
        