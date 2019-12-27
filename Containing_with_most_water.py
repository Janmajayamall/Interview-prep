class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxv = 0
        i = 0
        j = len(height)-1
        
        while(i<j):
            
            if height[i]>height[j]:
                if maxv<height[j]*(j-i):
                    maxv = height[j]*(j-i)
                j-=1
            
            if height[i]<=height[j]:
                if maxv<height[i]*(j-i):
                    maxv = height[i]*(j-i)
                i+=1
        return maxv
                