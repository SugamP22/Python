a={1:434,2:232,3:234}
b={4:424,5:132,6:134}

# a.update(b) 
# print(a)
for i in b:
  a[i]=b[i]
  
print(a)
print(a.items())
print(a.get(4))
print(a[4])
print(a.keys())
print(a.values())