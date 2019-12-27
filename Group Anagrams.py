class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anag = {}
        
        for i in strs:
            a = i
            a = ''.join(sorted(a))
            
            if a in anag:
                anag[a].append(i)
            else:
                anag[a]=[i]
        
        final_list=[]
        for key in anag.keys():
            final_list.append(anag[key])
        return final_list
            