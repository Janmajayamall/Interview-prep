class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #running from left list
        left_list = []
        
        #running from right list
        right_list = []
        
        for i in nums:
            if len(left_list)==0:
                left_list.append(i)
            else:
                left_list.append(left_list[-1]*(i))
            
        i=len(nums)-1
        while(i>=0):
            if len(right_list)==0:
                right_list.append(nums[i])
            else:
                right_list.append(right_list[-1]*nums[i])
            i-=1
            
        right_list = right_list[::-1]
            
        final_list=[]
        
        for j in range(len(nums)):
            
            if j==0:
                final_list.append(right_list[j+1])
            elif (len(nums)-1)==j:
                final_list.append(left_list[j-1])
            else:
                final_list.append(right_list[j+1]*left_list[j-1])
        
        return final_list
            