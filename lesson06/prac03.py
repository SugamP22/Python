# wap to write a factorial fo N
def factorial(a):
  res=1
  for i in range (1,a+1):
    res*=i
  return res

print(factorial(5))