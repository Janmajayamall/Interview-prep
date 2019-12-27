def checkPalindrome(value):
  i = 0
  j = len(value)-1

  while(i<j):

    if value[i]!=value[j]:
      return False 
    i+=1
    j-=1
  return True

def permutePali(string, curr):

  if len(string)==0:

    if checkPalindrome(curr):
      return True

    return 
  
  for i in range(len(string)):
    curr+=string[i]
    temp = string[:i]+string[i+1:]
    result = permutePali(temp, curr)
    if result!=None:
      return result
    curr=curr[:-1]
    
print(permutePali('aab', ''))