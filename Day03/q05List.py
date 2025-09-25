a=[1,2,3,4,5]
for i in range(len(a)-1):
  if a[i]>a[i+1]:
    print("List is not sorted")
    break
else:
  print("Yes the list is sorted!!")

 
