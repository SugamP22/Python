def suma(a,b):
  return a+b
def resta(a,b):
  return a-b
def multi(a,b):
  return a*b
def division(a,b):
  if(b==0):
    return "Invalido"
  else:
    return a/b

print(suma(2,2))
print(resta(5,2))
print(multi(3,5))
print(division(2,2))