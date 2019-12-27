class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = []
        max_right = []
        max_ = 0
        for i in height:
            max_left.append(max_)
            if i>max_:
                max_=i
        i = len(height)-1
        max_=0
        while(i>=0):
            max_right=[max_]+max_right
            if height[i]>max_:
                max_=height[i]
            i-=1

        i=0
        water = 0      
        while(i<len(height)):

            volume = min(max_left[i], max_right[i])
            volume-=height[i]
            
            
            if volume>0:
                water+=volume
                
            i+=1
        return water
                