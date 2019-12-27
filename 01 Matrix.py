class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        explored_dict = {}
        
        def dfs(graph, row, col, explored, depth):
            
            if (row, col) in explored_dict:
                return explored_dict[(row, col)]
            
            if row<0 or col<0 or row>=len(graph) or col>=len(graph[row]) or (row,col) in explored:
                return 1000000000000000000000
            
            if graph[row][col]==0:
                return depth
            
            explored.add((row,col))
            
            up=dfs(graph, row+1, col , explored, depth+1)
            down=dfs(graph, row-1, col , explored, depth+1)
            right=dfs(graph, row, col+1 , explored, depth+1)
            left=dfs(graph, row, col-1 , explored, depth+1)
            
            explored.remove((row,col))
            
            return min(up, down, right, left)
    
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                val = dfs(matrix, row, col, set(), 0)
                explored_dict[(row, col)]=val
                matrix[row][col]=val
        
        return matrix