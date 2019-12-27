class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0]<=nums[len(nums)-1]:
            return nums[0]
        
        def bins(vals, start, end):
            
            if end<start:
                return
            
            if end==start:
                return vals[end]
            
            mid = (start+end)//2
            
            if vals[mid]<vals[0] and vals[mid]<vals[mid-1]:
                print(vals[mid], 'w')
                return vals[mid]
            
            if vals[mid]>=vals[0]:
                return bins(vals, mid+1, end)
            else:
                return bins(vals, start, mid-1)
        
        
        val = bins(nums, 0, len(nums)-1)
        
        return None