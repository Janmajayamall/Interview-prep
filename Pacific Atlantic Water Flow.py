class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        our_set = {}
        final=[]
        
        def dfs(graph, row, col, last_indexes, new_set):
            # print([row, col], last_indexes)
            # if (row, col) in our_set:
            #     return our_set[(row, col)]
            
            pacific = False
            atlantic = False
            
            if row<0 or col<0 or row>=len(graph) or col>=len(graph[row]) or (row, col) in new_set:
                return [False, False]
        
            # checking whether it reached pacific and Atlantic
        
            # checking whether it just reached pacific
            if row==0 or col==0:
                pacific=True
            
            # checking whether it just reached atlantic
            if row==len(graph)-1 or col==len(graph[row])-1:
                atlantic=True
            
            if last_indexes!=None:                            
                if graph[row][col]>graph[last_indexes[0]][last_indexes[1]]:
                    return [False, False]
            
            if pacific and atlantic:
                return [True, True]
            
            
            new_set.add((row, col))

            up=dfs(graph, row-1, col, [row, col], new_set)
            down=dfs(graph, row+1, col, [row, col], new_set)
            right=dfs(graph, row, col+1, [row, col], new_set)
            left=dfs(graph, row, col-1, [row, col], new_set)
            
            our_set[(row, col)] = [pacific or up[0] or down[0] or right[0] or left[0] ,atlantic or up[1] or down[1] or right[1] or left[1]]
            
            return [pacific or up[0] or down[0] or right[0] or left[0], atlantic or up[1] or down[1] or right[1] or left[1]]
        
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                # if (row, col) in our_set:
                #     val = our_set[(row, col)]
                #     if val == [True, True]:
                #         final.append([row, col])
                # else:
                    val = dfs(matrix, row, col, None, set())
                    # print(val, row, col)
                    if val == [True, True]:
                        final.append([row, col])
        
        print(our_set)
            
            
        return final
                            
    
        
            
                
                
            
            
            
        
        