a=[1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
dic={}
for i in a:
  if i in dic.keys():#we need a if else because done diretly it can edit the value raturn then creating one!!
    dic[i]+=1
  else:
    dic[i]=1
print(dic)