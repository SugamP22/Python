# wap to print n to 1 backwards

def back(n):
  if(n<1):
    return
  print(n)
  back(n-1)

back(5)