class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def calc(val,p):
            if p == 0:
                return 1
            
            mid = p/2
            
            result = calc(val, mid)
            
            if p%2==0:
                return result*result
            else:
                return result*result*val

        if n>0:
            return float(calc(x, n))
        else:
            return float(1/calc(x, n*-1))