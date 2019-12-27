class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        max_v = 0
        rec = set()
        curr = 0
        last_ref = None
        while(i<len(s)):
            if s[i] not in rec:
                if len(rec)==0:
                    last_ref=i
                rec.add(s[i])
                curr+=1
            else:
                i=last_ref
                if max_v<curr:
                    max_v=curr
                curr=0
                rec=set()
            i+=1
        if curr>0:
            if max_v<curr:
                max_v=curr
        return max_v
                
                
            