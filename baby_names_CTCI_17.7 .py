def dfs(name, hashmap, synmap, explored_list, curr, freqmap):

  if curr in explored_list:
    return
  
  explored_list.append(curr)
  synmap[name]+=freqmap[curr]

  for i in hashmap[curr]:
    dfs(name, hashmap, synmap, explored_list,i)

def baby_names(names, synonyms):
  syn_names_map=get_syn_names_map(synonyms)

  explored_list=[]
  synmap={}
  for  key in syn_names_map.keys():
    if key not in explored_list:
      synmap[key]=0
      dfs(key, syn_names_map, synmap, explored_list, key)
  
  return synmap


    



