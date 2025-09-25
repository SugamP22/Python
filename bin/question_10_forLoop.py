num=int(input("Enter a number: "))
factor=0
for i in range(1,num+1):
  if(num%i==0):
    factor+=1
if factor==2:
  print(f"yes, the number {num} is a prime number")
else:
  print(f"No, the number {num} is not a prime number!!")
  