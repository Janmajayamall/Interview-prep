class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        numList = []
        
        first = 0
        second = 0 
        
        while(first<len(nums1) and second<len(nums2)):
            
            if nums1[first]<nums2[second]:
                numList.append(nums1[first])
                first+=1
                continue
            
            else:
                numList.append(nums2[second])
                second+=1
                continue
        
        if first<len(nums1):
            
            while(first<len(nums1)):
                numList.append(nums1[first])
                first+=1
        
        if second<len(nums2):
            
            while(second<len(nums2)):
                numList.append(nums2[second])
                second+=1
        
        if len(numList)%2==0:
            length = len(numList)/2
            return (float(numList[length]+numList[length-1])/2)
    
        else:
            return numList[len(numList)/2]
            
        