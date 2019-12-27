class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
    
        def isPali(string):
            
            i = 0
            j = len(string)-1
            
            while(i<j):
                if string[i]!=string[j]:
                    return False
                i+=1
                j-=1
            
            return True
        
        final_list=[]
        
        def find(index, val, curr):
            
            if index>=len(val):
                final_list.append(curr[::])
                return
            
            for i in range(index, len(val)):
                if isPali(val[index:i+1]):
                    curr.append(val[index:i+1])
                    find(i+1, val, curr)
                    curr.pop()
                
        find(0, s, [])
        return final_list
                
                
            