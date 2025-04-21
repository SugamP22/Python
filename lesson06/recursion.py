# writing a table using recursion
def table(n,M):
  if M>10:
    return
  print(f"{n} x {M} = {M*n}")
  table(n,M+1)


num=int(input("Ingresa un numero: "))
table(num,1)