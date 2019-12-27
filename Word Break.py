class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s)==0 and len(wordDict)!=0: 
            return False
        
        explored=set()
        
        def findV(val, wordD):
            
            if len(val)==0:
                return True
            
            curr = ''
            for i in range(len(val)):
                
                curr+=val[i]
                if curr in wordDict:
                    if val[i+1:] in explored:
                        return None
                    result = findV(val[i+1:], wordDict)
                    if result!=None:
                        return result
                    else:
                        explored.add(val[i+1:])
                        
            
        return findV(s, wordDict)
                
                
                
                