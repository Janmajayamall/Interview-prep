class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ns = str(n)
        
        MAX=100000000000000000000000000
        
        global final
        
        final=[]
        
        def check(val, curr):
            
            if len(val)==0:
                
                if int(curr)>n:
                    final.append(curr)
                return
            
            for i in range(len(val)):
                    
                temp = val[:i]+val[i+1:]
                curr+=val[i]
                resu = check(temp, curr)
                curr=curr[:-1]

        
        check(ns, '')
        
        
        if final==[]:
            return -1
        
        return min(final)