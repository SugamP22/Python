# Print positive and negative elements of an list
a=[1,-1,2,-2,3,-3,4,-4,5,-5]
positive=[]
negative=[]

for i in range(len(a)):
  if(a[i]>0):
    positive.append(a[i])
    continue
  negative.append(a[i])
print(f"Original list: {a}")
print(f"List of positive numbers: {positive}")
print(f"List of negative numbers: {negative}")
    