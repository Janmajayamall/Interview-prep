class Solution(object):    #failing few test cases
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        def compare(ch, cu):
            
            for i in ch.keys():
                if i not in cu:
                    return False
                if ch[i]>cu[i]:
                    return False
            
            return True
        
        
        start = 0 
        end =0 
        
        checkSet={}
        for i in t:
            if i in checkSet:
                checkSet[i]+=1
            else:
                checkSet[i]=1
        
        smallest=''
        
        currSet={}
        curr = ''
        
        while(start<len(s) and end<len(s)):    
            
            if compare(checkSet, currSet):
                print(currSet, curr)
                if smallest == '' or len(smallest)>len(curr):
                    smallest=curr
                
                curr=curr[1:]
                
                if s[start] in currSet:
                    currSet[s[start]]=currSet[s[start]]-1
                    if currSet[s[start]] == 0:
                        del currSet[s[start]]
                start+=1
                continue
                
            else:
                
                curr+=s[end]
                if s[end] in checkSet:
                    if s[end] in currSet:
                        currSet[s[end]]=currSet[s[end]]+1
                    else:
                        currSet[s[end]]=1
                end+=1
        
        if start<len(s) and compare(checkSet, currSet):
            
            while currSet.keys()==checkSet.keys() and start<len(s):
                
                if smallest == '' or len(smallest)>len(curr):
                    smallest=curr
                
                curr=curr[1:]
                
                if s[start] in currSet:
                    currSet[s[start]]=currSet[s[start]]-1
                    if currSet[s[start]] == 0:
                        del currSet[s[start]]
                start+=1
                
        return smallest
            
            