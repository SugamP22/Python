a={1:434,2:232,3:234,4:424}
b={4:425,5:132,6:134}
  
for i in b:
  if i in a.keys():
    a[i]+=b[i]
  else:
    a[i]=b[i]

  
print(a)