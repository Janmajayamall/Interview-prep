class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        final=[]
        
        for i in range(len(matrix)):
            temp=[]
            for j in range(len(matrix[i])):
                temp.append(matrix[i][j])
            final.append(temp)
            
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j]=final[len(matrix)-1-j][i]
        return matrix
        