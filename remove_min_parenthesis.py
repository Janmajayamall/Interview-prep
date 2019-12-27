
class Parenthesis():
    def __init__(self, ch, pos):
        self.char = ch
        self.pos = pos

class Stack():
    def __init__(self):
        self.stack=[]
    
    def push(self, char, pos):
        self.stack.append(Parenthesis(char, pos))
    
    def pop(self):
        temp=self.stack[-1]
        self.stack=self.stack[:-1]
        return temp
    
    def isempty(self):
        return len(self.stack)==0
        
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack=Stack()
        remove_pos  = []
        
        pos = 0
        while pos<len(s):
            
            if s[pos]=="(":
                stack.push(s[pos], pos)
            
            if s[pos]==")":
                if not stack.isempty():
                    stack.pop()
                else:
                    s=s[:pos]+s[pos+1:]
                    pos-=1

            pos+=1
            
        count = 0
        while not stack.isempty():
            item = stack.pop()
            s = s[:item.pos-count]+s[item.pos+1-count:]
        return s
                
                
        
            
            
        
        