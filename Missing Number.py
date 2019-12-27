class Solution(object):
    # normal approach
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_v = max(nums)
#         check = [0]
#         for i in nums:
#             check.append(0)
            
#         for i in nums:
#             check[i]=1
        
#         for i in range(len(check)):
#             if check[i]==0:
#                 return i
#         return max_v+1
                        
    #Gauss formula
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_v = len(nums)
        
        sum1 = ((max_v)*(max_v+1))/2
        sum2 = 0
        for i in nums:
            sum2+=i
        return sum1-sum2
    