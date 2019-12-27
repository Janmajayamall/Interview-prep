class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #storing the frequency of each value in the list
        hashmap = {}
        
        for i in nums:
            
            if i in  hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
          
        list_tup = []
        for i in hashmap.keys():
            list_tup.append((i, hashmap[i]))
            
        list_tup=sorted(list_tup, key= lambda x:x[1], reverse=1)

        final_list=[]
        
        for i in range(0, k):
            final_list.append(list_tup[i][0])
        
        return final_list
            
            
            