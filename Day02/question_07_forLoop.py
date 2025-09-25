num=int(input("Enter a number: "))
even=0
odd=0
for i in range(1,num+1):
  if(i%2==0):
    even+=i
  else:
    odd+=i
    
print(f"The sum of all even number upto {num} is {even}")
print(f"The sum of all odd number upto {num} is {odd}")