def longest_word(word_dict, word_list):

  def permute(curr, word_list, word_dict):
    # print(curr)
    if len(word_list)<=0:
      return 0
    
    mac_len=-100000000000000000
    for i in range(len(word_list)):
      
      if (curr+word_list[i] in word_dict) and len(curr+word_list[i])>mac_len:
        mac_len=len(curr+word_list[i])
      
      result=permute(curr+word_list[i], word_list[:i]+word_list[i+1:], word_dict)
      if result>mac_len:
        mac_len=result
    
    return mac_len

  result=permute("", word_list, word_dict)
  if result!=-100000000000000000:
    return result
  return -1

wd=set()
wd.add("cat")
wd.add("banana")
wd.add("dog")
wd.add("nana")
wd.add("walk")
wd.add("walker")
wd.add("dogwalker")

wl=["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]

print(longest_word(wd, wl))


