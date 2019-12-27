class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums[0]<=nums[len(nums)-1]:
            return nums[0]
        
        def searchBin(vals, start, end):
            
            if end<=start:
                return None
            
            if (end-start)<=1:
                return min(vals[start], vals[end])
            
            mid = (end+start)//2

            if vals[mid]<vals[mid-1] and vals[mid]<vals[0]:
                return vals[mid]
            else:
                if vals[mid]>=vals[0]:
                    return searchBin(vals, mid, end)
                else:
                    return searchBin(vals, start, mid)
            
        return searchBin(nums, 0, len(nums)-1)