
def circus_tower(array):

  array.sort(key=lambda x:(x[0],x[1]))
  dp=[]
  for i in array:
    dp.append(1)
  
  for i in range(len(array)):
    j=0
    while(j<i):
      if array[j][0]<array[i][0] and array[j][0]<array[1][1]:
        if dp[j]+1>array[i]:
          dp[i]=dp[j]+1
      j+=1
  
  return max(dp)



  

  