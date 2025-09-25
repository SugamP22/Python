a=int(input("Enter a number: "))
original=a
rev=0
while(a!=0):
  rev=rev*10+(a%10)
  a=a//10
if original==rev:
  print("Yes, its a palindrome")
else:
  print("No, its not a palindrome!!")
