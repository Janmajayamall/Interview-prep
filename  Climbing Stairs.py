class Solution:
    def climbStairs(self, n: int) -> int:
        
        explored_set = {}
        def climb(curr, n):
            
            if curr==n:
                return 1
        
            if curr in explored_set:
                return explored_set[curr]
            
            if curr>n:
                return 0
            
            result = 0
            for i in [1, 2]:
                curr+=i
                result+=climb(curr, n)
                curr-=i
            explored_set[curr]=result
            return result
           
        return climb(0, n)