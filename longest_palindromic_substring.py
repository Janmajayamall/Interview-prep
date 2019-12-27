class Solution:

        def longestPalindrome(self, s: str) -> str:
    
            if s=="":
                return ""

            dp_matrix = []

            for i in range(len(s)):
                temp = []
                for j in range(len(s)):
                    temp.append(0)
                dp_matrix.append(temp)

            final_str = ''
            for i in range(len(s)):
                for j in range(len(s)):
                    a = j
                    b = a+i

                    if b<len(s):

                        if i == 0:
                            dp_matrix[a][b]=1
                            if len(final_str)==0:
                                final_str=s[a]
                            continue

                        if i == 1:
                            if (s[a]==s[b]):
                                dp_matrix[a][b]=2
                                if len(final_str)<2:
                                    final_str=s[a:b+1]
                            else:
                                dp_matrix[a][b]=0

                        if i > 1:
                            if s[a]==s[b] and dp_matrix[a+1][b-1]>0:
                                dp_matrix[a][b]=(b-a)+1
                                if len(final_str)<((b-a)+1):
                                    final_str=s[a:b+1]
                            else:
                                dp_matrix[a][b]=0

                    else:
                        break
            return final_str

