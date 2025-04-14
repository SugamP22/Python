num=int(input("Introduce un numero: "))
count=1
while count<=10:
  print(f"{num} x {count} =   {num*count}")
  if(count==10):
    break
  count+=1