class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        dependencyMap={}
        
        for i in prerequisites:
            if i[0] in dependencyMap:
                dependencyMap[i[0]].append(i[1])
            else:
                dependencyMap[i[0]]=[i[1]]
        
        completedCourses = []
        
        def dfs(curr,completedCourses ):
            
            if curr in completedCourses:
                return []
        
            if curr not in dependencyMap or len(dependencyMap[curr])==0:
                return []
        
            stack = dependencyMap[curr]
            explored = [curr]
    
            while(len(stack)!=0):
                
                temp = stack[-1]
                stack= stack[:-1]
                
                if temp in completedCourses:
                    continue
                
                if (temp in explored) and (temp in dependencyMap):
                    return False
                
                explored.append(temp)
                if temp in dependencyMap:
                    stack+=dependencyMap[temp]  
            return explored
        
        for i in range(numCourses):
            result = dfs(i, completedCourses)
            if result==False:
                return False            
            completedCourses+=result
        
        return True

            