class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def selection_sort(vals):  #time O(n)  #space O(n)
            
            count=0
            
            while(count!=len(vals)):
                minV=100000000000000000
                index=None
                for i in range(count, len(vals)):
                    
                    if vals[i]<minV:
                        minV=vals[i]
                        index=i

                if index!=count:
                    temp=vals[index]
                    vals[index]=vals[count]
                    vals[count]=temp
                count+=1
            
            return vals
    
        return selection_sort(nums)