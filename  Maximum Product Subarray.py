class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        current_max = -1000000000000000
        current_min = 1000000000000000
        
        product_max = None
        
        for i in nums:
            
            if product_max==None:
                current_max=i
                current_min=i
                product_max=i
            else:
                temp = current_max
                current_max = max(current_max*i, current_min*i, i)
                current_min = min(temp*i, current_min*i, i)
                
                if current_max>product_max:
                    product_max=current_max
            
        return product_max