class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        citations.sort()
        
        i = len(citations)-1
        count = 0
        
        while(i>=0):
            count+=1
            if citations[i]==count:
                return count
            elif citations[i]<count:
                return count-1
            else:
                i-=1
                
        return count
            