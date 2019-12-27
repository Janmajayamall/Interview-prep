class Solution(object):
    def threeSumClosest(self, target, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        final_list = None
        diff = 10000000000000000000000000000
        target.sort()
        for i in range(len(target)):
            
            if i!=0 and target[i]==target[i-1]:
                continue
            
            start = i+1
            end = len(target)-1
            
            while(start<end):
                
                if start!=i+1 and target[start-1]==target[start]:
                    start+=1
                    continue 
                    
                if end!=len(target)-1 and target[end]==target[end+1]:
                    end-=1
                    continue 
                    
                total = target[i]+target[start]+target[end]
                
                if abs(nums-total)<diff:
                    diff=abs(nums-total)
                    final_list = [target[i],target[start],target[end]]
                
                if total>nums:
                    end-=1
                    continue 
                
                if total<nums:
                    start+=1
                    continue
                su = 0 
                for i in [target[i],target[start],target[end]]:
                    su+=i
                return su

        if final_list==None:
            return None
        
        sum_ = 0
        
        for i in final_list:
            sum_+=i
        
        return sum_
                    
                