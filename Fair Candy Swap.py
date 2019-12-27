class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        A.sort()
        B.sort()
        
        targetVal = (sum(A)-sum(B))/2
        
        a=0
        b=0
        
        while a<len(A) and b<len(B):
            
            val = A[a]-B[b]
            
            if val<targetVal:
                a+=1
            elif val>targetVal:
                b+=1
            else:   
                return [A[a], B[b]]
        
        return None
        