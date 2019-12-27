

def makeit(emplist, topl):

  def bfs(ed, td, final_list, cur):
    explore = []
    if len(cur)==0:
      return 
    for curr in cur:
      print(curr)
      if curr in td:
        if len(td[curr])>0:
          for val in td[curr]:
            if val in ed:
              final_list+=ed[val]
            explore.append(val)

    bfs(ed, td, final_list, explore)

  empDict={}

  for i in emplist:

    if i[1] in empDict:
      empDict[i[1]].append(i)
    else:
      empDict[i[1]]=[i]
  
  topDict={}

  for post in topl:

      if post[1] in topDict:
        topDict[post[1]].append(post[0])
      else:
        topDict[post[1]]=[post[0]]
  final=[]
  bfs(empDict, topDict, final, ["CEO"])
  final=final[::-1]
  final.append(empDict["CEO"])
  return final
  


employees = [('John', 'Manager'), ('Sally', 'CTO'), ('Sam', 'CEO'), ('Drax', 'Engineer'), ('Bob', 'CFO'), ('Daniel', 'Engineer'), ('awdw', 'a')]

topology = [['CTO', 'CEO'], ['Manager', 'CTO'], ['Engineer', 'Manager'], ['CFO', 'CEO'], ['a', 'CFO']]

print(makeit(employees, topology))