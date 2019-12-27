"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node==None:
            return
        
        copyDict = {}
        
        def dfs(head, copy=False):
            explored_dict = set()
            if head==None:
                return 
            
            stack = [head]
            
            while(len(stack)!=0):
                current = stack[-1]
                stack=stack[:-1]
                
                if current in explored_dict:
                    continue
                
                for i in current.neighbors:
                    stack.append(i)

                if copy:
                    explored_dict.add(current)
                    temp=[]
                    for i in current.neighbors:
                        temp.append(copyDict[i])
                    copyDict[current].neighbors=temp
                else:
                    explored_dict.add(current)
                    copyDict[current]=Node(current.val, [])
        
        dfs(node)
        
        dfs(node, True)
        
        return(copyDict[node])
        
            
            
                
            
            
            
        