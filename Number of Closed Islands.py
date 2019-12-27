class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
     
        def dfs(graph, row, col):
            
            if row<0 or col<0 or row>=len(graph) or col>=len(graph[row]):
                return False
            
            if graph[row][col]==1:
                return True
            
            graph[row][col]=1
            
            up=dfs(graph, row-1, col)
            down=dfs(graph, row+1, col)
            right=dfs(graph, row, col+1)
            left=dfs(graph, row, col-1)
            
            
            if up and down and right and left:
                return True
            else:
                return False
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0:
                    if dfs(grid, i, j):
                        count+=1
    
        return count
            
            
            
            