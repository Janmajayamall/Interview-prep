class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        for i in range(len(prices)):
            
            if i!=0 and prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
                
        return profit
    
        