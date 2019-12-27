class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #bubble sort
        
        def helper(vals):
            
            for i in range(len(vals)):
                if i==0:
                    continue
                
                if vals[i]<vals[i-1]:
                    return False
            return True
        
        def bubble_sort(vals): # worst time complexity n^2 & worst space complexity n
            index=0
            
            while(not helper(vals)):
                
                if index==0:
                    index+=1
                    continue
                
                if vals[index]<vals[index-1]:
                    temp=vals[index]
                    vals[index]=vals[index-1]
                    vals[index-1]=temp
                
                index+=1
                
                if index==len(vals):
                    index=0
            
            return vals
    
        return bubble_sort(nums)
                