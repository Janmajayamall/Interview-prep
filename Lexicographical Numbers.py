class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        final_list=[]
        
        def sortT(val, v):
            
            for i in range(10):
                
                if val=='' and i==0:
                    continue
                    
                val+=str(i)
                
                if int(val)>v:
                    return
                
                final_list.append(int(val))
                sortT(val, v)
                
                val=val[:-1]
        
        sortT('', n)
            
        return final_list
                