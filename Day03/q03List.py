a=[1,11,223,432,344,23]
b=a[0]
for i in range(len(a)):
  if b> a[i]:
    continue
  b=a[i]

  
print(f"The greatest number among all these value in the list {a} is {b} its located in {a.index(b)}")
    