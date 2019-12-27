class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(0)
            grid.append(temp)
        
        grid[0][0]=1
        
        for row in range(n):
            for col in range(m):
                if row==0 and col==0:
                    continue
                ways = 0
                if row>0:
                    ways+=grid[row-1][col]
                if col>0:
                    ways+=grid[row][col-1]
                grid[row][col]=ways
            
        print(grid)
            
        return grid[n-1][m-1]