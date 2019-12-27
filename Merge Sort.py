class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def merge(vals, low, mid, high):
            
            helper1=[]
            helper2=[]
            for i in range(low, mid+1):
                helper1.append(vals[i])
            for i in range(mid+1, high+1):
                helper2.append(vals[i])
            
            a=0
            b=0
            curr=low
            while(a<len(helper1) and b<len(helper2)):
                
                minV=10000000000000000
                
                if helper1[a]<helper2[b]:
                    minV=helper1[a]
                    a+=1
                else:
                    minV=helper2[b]
                    b+=1
                
                vals[curr]=minV
                curr+=1
            
            if a!=len(helper1):
                
                while(a<len(helper1)):
                    vals[curr]=helper1[a]
                    a+=1
                    curr+=1
            
            if b!=len(helper2):
                
                while(b<len(helper2)):
                    vals[curr]=helper2[b]
                    b+=1
                    curr+=1                                                
        
        def merge_sort(vals, low, high):

            if (high-low)==0:
                return
            
            if low<high:
                mid=(high+low)//2
                merge_sort(vals, low, mid)
                merge_sort(vals, mid+1, high)
                merge(vals, low, mid, high)
            
        merge_sort(nums, 0, len(nums)-1)
        return nums
                
            