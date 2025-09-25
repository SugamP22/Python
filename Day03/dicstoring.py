a={1:"Hello",2:"Bye"}
print(a)
print(a[1])
a[1]="Bhak"#editing
a[3]="Au mero babu"#updating
print(a)
del a[2]#deleting
print(a)
for i in a:
  print(a[i])
  
for i in a:
  print(i)
  
for i in a.values():
  print(i)