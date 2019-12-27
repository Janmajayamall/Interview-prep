class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        def bs(vals, low, high):
            print(low, high)
            if low<=high:

                mid=(high+low)//2
                if mid>0 and mid<(len(vals)-1):
                    print(vals[mid])
                    if vals[mid-1]<vals[mid] and vals[mid]>vals[mid+1]:
                        return mid
                
                    if vals[mid-1]<vals[mid]:
                        return bs(vals, mid+1, high)
                    else:
                        return bs(vals, low,mid-1)
            else:
                return -1
            
        return bs(A, 0, len(A)-1)
                    
            
            
        
        
        slope=False
        peak=None
        for i in range(len(A)):
            
            if i==0:
                continue
            
            if A[i]>A[i-1] and not slope:
                continue
            elif A[i]<A[i-1]:
                if slope!=True:
                    peak=i-1
                    slope=True     
            else:
                return -1
            
        return peak