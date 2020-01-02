class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def compare_set(map1, map2):
            for key in map1.keys():
                if key in map2 and map1[key]<=map2[key]:
                    pass
                else:
                    return False
            return True
        
        def decrease_freq_map(map1, char):
            if char in map1:
                map1[char]-=1
                if map1[char]==0:
                    del[map1[char]]
        
        def increase_freq_map(map1, char):
            if char in map1:
                map1[char]+=1
            else:
                map1[char]=1
        
        def find_min_window(s, t):
            start=0
            end=0
            curr={}
            sub={}
            curr_str=""
            min_str=""
            for i in t:
                increase_freq_map(sub, i)

            
            while(end<=len(s)):
                
                if not compare_set(sub, curr) and end<len(s):
                    increase_freq_map(curr, s[end])
                    curr_str+=s[end]
                    end+=1
                elif compare_set(sub, curr):
                    if min_str=="" or len(curr_str)<len(min_str):
                        min_str=curr_str
                    decrease_freq_map(curr, s[start])
                    curr_str=curr_str[1:]
                    start+=1
                else:
                    end+=1
            
            return min_str
    
        return find_min_window(s,t)
                    
            

                
                
                
            