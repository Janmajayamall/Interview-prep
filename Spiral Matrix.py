class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix)==0:
            return
        
        startRow=0
        endRow=len(matrix)-1
        startCol=0
        endCol=len(matrix[0])-1
        finalList=[]
        while(startRow<=endRow and startCol<=endCol):

            for i in range(startCol, endCol+1):
                finalList.append(matrix[startRow][i])
            startRow+=1


            for i in range(startRow, endRow+1):
                finalList.append(matrix[i][endCol])
            endCol-=1
            
            if startRow<=endRow:
                i=endCol   
                while(i>=startCol):
                    finalList.append(matrix[endRow][i])
                    i-=1
                endRow-=1
 
            
            if startCol<=endCol:
                i=endRow
                while(i>=startRow):
                    finalList.append(matrix[i][startCol])
                    i-=1
                startCol+=1
           

        return finalList
    
                    