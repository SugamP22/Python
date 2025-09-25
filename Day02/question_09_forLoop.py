num=int(input("Enter a number: "))
sum=0
for i in range(1,num):
  if(num%i==0):
    sum+=i
if(sum==num):
  print(f"Yes, number {num} is  a perfect number because the total sum of its factors is {sum}")
else:
  print(f"No, number {num} is not a perfect number because the total sum of its factors is {sum}")