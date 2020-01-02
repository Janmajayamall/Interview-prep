def letterAndNumbers(string):
  diff_map={0:-1}
  alpha_c=0
  num_c=0
  longest=-100000000000000000
  for index,i in enumerate(string):
    try:
      val=int(i)
      num_c+=1
    except:
      alpha_c+=1
    
    diff = alpha_c-num_c

    if diff in diff_map:
      if (index-diff_map[diff])>longest:
        longest=index-diff_map[diff]
      else:
        diff_map[diff]=index

  return longest

l=letterAndNumbers(['a', '1', 'a', 'a', 'a', 'a', 'a', '1', '1', '1', '1', '1', '1', 'a', 'a'])
print(l)