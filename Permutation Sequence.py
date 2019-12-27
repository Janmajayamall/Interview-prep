class Solution(object):      # time limit exceeded
    
    def __init__(self):
        self.k = None
        self.final=None
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        self.k = k
        
        valueArr = []
        for i in range(n):
            valueArr.append(i+1)
        
        def permutation(currPer, vals):

            if (len(currPer)==n):
                self.k-=1
                
                if self.k == 0:
                    self.final=currPer
                return 1

            for i in range(len(vals)):
                
                temp = vals[:i]+vals[i+1:]
                
                permutation(currPer+str(vals[i]), temp)
                
                if self.k==0:
                    return
        
        permutation("", valueArr)

        return self.final
            
 