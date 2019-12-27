class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def partition(vals, low, high):
            
            if high<=low:
                return
        
            mid=(high+low)//2
            
            temp=vals[mid]
            vals[mid]=vals[low]
            vals[low]=temp
            
            pointer1=low
            pointer2=low+1
            while(pointer2<(high+1)):
                
                if vals[pointer2]>vals[low]:
                    pointer2+=1
                else:
                    pointer1+=1
                    temp=vals[pointer2]
                    vals[pointer2]=vals[pointer1]
                    vals[pointer1]=temp
                    pointer2+=1
                
            temp=vals[pointer1]
            vals[pointer1]=vals[low]
            vals[low]=temp
        
            return pointer1
    
        def quicksort(vals, low, high):                
            
            if high>low:
                part=partition(vals, low, high)
                quicksort(vals, low, part-1)
                quicksort(vals, part+1, high)
                
        quicksort(nums, 0, len(nums)-1)
        return nums
            
                    
            