class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def dfs(grid, row, col, explored, w):
            
            if len(w)==0:
                return True
            
            if row<0 or col<0 or row>=len(grid) or col>=len(grid[row]) or (row, col) in explored or grid[row][col]!=w[0]:
                return False
            
            explored.add((row, col))
            
            down = dfs(grid, row+1, col, explored, w[1:])
            up = dfs(grid, row-1, col, explored, w[1:])
            right = dfs(grid, row, col+1, explored, w[1:])
            left = dfs(grid, row, col-1, explored, w[1:])
        
            explored.remove((row, col))
        
            return up or down or right or left
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    if dfs(board, i, j, set(), word):
                        return True
        
        return False