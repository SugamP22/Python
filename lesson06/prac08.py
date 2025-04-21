# calculting the sum of first n num using recursion
def sum(n):
  if(n==0):
    return 0
  else:
    return sum(n-1)+n

print(sum(10))
    