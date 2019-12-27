class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:     THIS METHOD RUNS SLOWER BY FEW ms (JUST COULD NOT PASS LAST 2 CASES, TIME LIMIT EXCEEDED)
#         nums.sort()
#         final_list=[]
#         def makeSums(vals, curr, index):
            
#             if len(curr)==3:
#                 sum_ = 0 
#                 for v in curr:
#                     sum_+=v
#                 if sum_==0:
#                     final_list.append(curr[::])
#                 return
            
#             for i in range(index, len(vals)):
                
#                 if i!=index and vals[i]==vals[i-1]:
#                     continue
                
#                 curr.append(vals[i])
#                 makeSums(vals, curr, i+1)
#                 curr.pop()
#         makeSums(nums, [], 0)
#         return final_list


        def threeSum(self, nums: List[int]) -> List[List[int]]: 
#             passed all test cases
            nums.sort()
            final_list=[]
            
            for i in range(len(nums)):
                
                if i!=0 and nums[i]==nums[i-1]:
                    continue
                    
                l=i+1
                j=len(nums)-1
                
                while(l<j):
                    
                    if l!=i+1 and nums[l]==nums[l-1]:
                        l+=1
                        continue
                    
                    if j!=len(nums)-1 and nums[j]==nums[j+1]:
                        j-=1
                        continue 
                    
                    
                    curr = nums[i]+nums[l]+nums[j]
                    
                    if curr>0:
                        j-=1
                        continue 
                    
                    if curr<0:
                        l+=1
                        continue 
                        
                    final_list.append([nums[i],nums[l],nums[j]])
                    l+=1
                    j-=1
                    
            return final_list
                    
                