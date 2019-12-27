class Solution:
    def reverseWords(self,a: str) -> str:
        
        a=a.split(" ")
        s=[]
        
        for i in a:
            if i==' ' or i=='':
                continue
            else:
                s.append(i)
            
        i = 0
        j = len(s)-1
        
        while(i<j):            
            temp = s[j]
            s[j]=s[i]
            s[i]=temp
            i+=1
            j-=1
            
        
        if len(s)==0:
            return ''
        
        final = s[0]
        
        for i in range(len(s)):
            
            if i == 0:
                continue
            
            final=final+' '+s[i]
        
        return final