class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in range(len(s)):
            
            if s[i]=='{' or s[i]=='[' or s[i]=='(':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                if stack[-1]=='{' and s[i]!='}':
                    return False
                if stack[-1]=='(' and s[i]!=')':
                    return False
                if stack[-1]=='[' and s[i]!=']':
                    return False
                
                stack=stack[:-1]
        
        if len(stack)!=0:
            return False
        
        return True