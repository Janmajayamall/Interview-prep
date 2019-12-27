class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            
        explored_strings={}
        
        def break_it(str1, str2):
            
            if (str1, str2) in explored_strings:
                return explored_strings[(str1, str2)]
            
            if len(str1)==0 or len(str2)==0:
                return 0
            if str1[0]==str2[0]:
                 explored_strings[(str1, str2)]=1+break_it(str1[1:], str2[1:])
            else:
                 explored_strings[(str1, str2)]=max(break_it(str1[1:], str2), break_it(str1, str2[1:]))
            return explored_strings[(str1, str2)]
        
        return break_it(text1, text2)
    