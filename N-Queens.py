class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        def check(marks, col, row):
            
            
            for val in marks:
                if val[1]==col:
                    return False
                
                if abs(val[0]-row)==abs(val[1]-col):
                    return False
            
            return True
            
        def permute(v, marks, cr, currVals, finallist):
            
            if cr==n:
                finallist.append(currVals[::])
                return
        
            if cr>n:
                return
            
            for i in range(v):
                
                if check(marks, i, cr):
                    
                    marks.add((cr, i))
                    currVals.append((cr, i))
                    permute(n, marks, cr+1, currVals, finallist)
                    currVals.pop()
                    marks.remove((cr, i))
        
        finallist  = []
        poss = permute(n, set(), 0, [], finallist)

        finalGrid=[]
        for prop in finallist:
            matrix = []
            for row in prop:
                text=''
                for i in range(n):
                    if row[1]==i:
                        text+='Q'
                    else:
                        text+='.'                
                matrix.append(text)
            finalGrid.append(matrix)
        
        return finalGrid
                    
                
                
                    
                    
                        