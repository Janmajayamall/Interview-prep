class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList:
            return 0
        
        wordSet = set()
        for i in wordList:
            wordSet.add(i)
        
        queue = [beginWord]
        
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        depth=1
        while(len(queue)!=0):
            
            size = len(queue)
            
            for i in range(size):
                
                currentWord = queue[0]
                queue=queue[1:]
                
                for charI in range(len(currentWord)):
                    
                    for i in range(ord('a'), ord('z')+1):
                        
                        newWord = currentWord[:charI] + chr(i) + currentWord[charI+1:]
                        if newWord==endWord:
                            return depth+1
                        
                        if newWord in wordSet:
                            queue.append(newWord)
                            wordSet.remove(newWord)
                            
            depth+=1
        
        return 0
                            
                        
                    
                    
                    
                    
        