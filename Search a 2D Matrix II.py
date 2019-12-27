class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix)==0:
            return False
        
        avoidCols=set()
        avoidRows=set()
        
        row = 0
        col = len(matrix[0])-1
        
        while(col>=0 and row<len(matrix)):
            
            if matrix[row][col]==target:
                return True
            
            if matrix[row][col]>target:
                col-=1
                continue
            else:
                row+=1
                continue
        
        return False
        
            
            