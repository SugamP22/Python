# wap to prac recursion from 1 to n number
i=1
def show(n,i):
  if(i>n):
    return
  print(i)
  show(n,i+1)
  
show(7,i)