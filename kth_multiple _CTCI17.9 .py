def kth_multiple(k):
  array_s=[1,3, 5, 7]
  array=[3, 5, 7]
  count=4
  last_ref=1
  index=0
  value=7
  
  if k<=4:
    return array_s[k-1]

  while(count<k):
    array_s.append(array[index%3]*array_s[last_ref])
    index+=1
    value=array_s[-1]
    if index%3==0:
      last_ref+=1
    count+=1
  return value

print(kth_multiple(7))




  

