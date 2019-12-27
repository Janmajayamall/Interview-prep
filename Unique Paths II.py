class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """ 
        
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[row])):
                if obstacleGrid[row][col]==1:
                    obstacleGrid[row][col]=-1
        
        if obstacleGrid[0][0]!=-1:
            obstacleGrid[0][0]=1
        else:
            return 0
            
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[row])):
                if obstacleGrid[row][col]==-1 or (row==0 and col==0):
                    continue
                total=0
                if row>=0 and obstacleGrid[row-1][col]!=-1:
                    total+=obstacleGrid[row-1][col]
                if col>=0 and obstacleGrid[row][col-1]!=-1:
                    total+=obstacleGrid[row][col-1]
                
                obstacleGrid[row][col]=total
           
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]!=-1:
            return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
        else:
            return 0