class Char():
  def __init__(self, char, count):
    self.char = char
    self.count = count

class Stack():

  def __init__(self):
    self.stack = []
  
  def push(self, ch):
    char = Char(ch, 1)
    self.stack.append(char)
  
  def pop(self):
    temp = self.stack[-1]
    self.stack=self.stack[:-1]
    final=""
    for i in range(temp.count):
      final+=temp.char
    return final
  
  def trim(self, k):
    if len(self.stack)==0:
      return False
    if self.stack[-1].count >= k:
      return self.pop()
  
  def isempty(self):
    return len(self.stack)==0

  def check(self, ch):
    if len(self.stack)==0:
      return False
    return self.stack[-1].char==ch
  
  def increase(self):
    self.stack[-1].count = self.stack[-1].count+1

def candy_crush(string, k):

  stack=Stack()

  for ch in string:
    if stack.check(ch):
      stack.increase()
    else:
      stack.trim(k)
      if stack.check(ch):
        stack.increase()
      else:
        stack.push(ch)

  stack.trim(k)    

  final_string = ''

  while not stack.isempty():
    temp = stack.pop()+final_string
    final_string=temp
  
  return final_string

if __name__ == "__main__":
    assert candy_crush("aaabbbc", 3) == "c"
    assert candy_crush("aabbbacd", 3) == "cd"
    assert candy_crush("baaabbbabbccccd", 3) == "abbd"
    assert candy_crush("", 3) == ""
    assert candy_crush("bbbbbbb", 3) == ""
    assert candy_crush("aaabbbacd", 3) == "acd"
    assert candy_crush("ccddccdcaacabbbaaccaccddcdcddd", 3) == ""
    print("done")


    