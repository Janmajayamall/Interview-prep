class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while(int(n/5)>0):
            
            count+=int(n/5)
            n=int(n/5)
            
        return count
                