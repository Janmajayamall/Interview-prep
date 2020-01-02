
class SendListOfString():

  def encode(self, str_list):
    final_str=""
    for string in str_list:
      final_str+=str(len(string))
      final_str+="/"
      final_str+=string
    
    return final_str
  
  def decode(self, encoded_string):
    string_list=[]
    index=0
    while(index<len(encoded_string)):
      if encoded_string[index]=="/":
        curr=index-1
        ref = ""
        while(curr>=0):
          try:
            int_v = int(encoded_string[curr])
            ref=encoded_string[curr]+ref
            curr-=1
          except:
            break
        if ref=="":
          return 
        ref=int(ref)       
        temp_string=""
        index+=1
        while(ref>0 and index<len(encoded_string)):
          temp_string+=encoded_string[index]
          index+=1
          ref-=1
        string_list.append(temp_string) 
        print(temp_string)
        continue
      else:
        index+=1
    return string_list
  
encode_decode=SendListOfString()
str_list=["dwadawd", "dawda//dawdawdawd", "dawd123r1fd@#@#", "dawdfavbfdcvsvb .    eawd", "dawdaw"]
value=encode_decode.encode(str_list)
print(value)
final_list=encode_decode.decode(value)
print(final_list)
        
          


