# Wap to calculate factorial of num n and using recursion
def fac(n):
  if n==1 or n==0:
    return 1
  else:
    return fac(n-1)*n
  
print(fac(5))