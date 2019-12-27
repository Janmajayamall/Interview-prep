

def find(val, curr, n):

  if val==n:
    return curr

  if val>n:

    temp = val 
    mark = curr
    while(temp>=n):
      if temp==n:
        return mark

      mark+=1
      temp=int(temp/3)

  val*=2
  curr+=1
  return find(val, curr, n)

print(find(1, 0, 10))





