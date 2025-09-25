a=[1,2,111,222,333,432,343]
largest=a[0]
secondlargest=a[0]
for i in range(len(a)):
  if(a[i]>largest):
    secondlargest=largest
    largest=a[i]
  elif(a[i]>secondlargest):
    secondlargest=a[i]
  
print(f"The second largest is {secondlargest}")