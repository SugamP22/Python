num=[1,2,3,4,5,6,7,8,9]
def sum(a,i):
  if(i==len(a)):
    return 
  else:
    print(a[i], end=" ")
    sum(a,i+1)
    
sum(num,0)

