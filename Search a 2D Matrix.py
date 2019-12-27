class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if len(matrix)==0:
            return False
        
        left = 0
        right = (len(matrix)*len(matrix[0]))-1
        distri = len(matrix[0])
        
        while left<=right:
        
                mid = left+((right-left)//2)
                
                midpoint=matrix[mid//distri][mid%distri]

                if midpoint==target:
                    return True
                if midpoint>target:
                    right=mid-1
                else:
                    left=mid+1

        
        return False