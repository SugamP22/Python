a=input("Enter a word: ")
b=""
for i in range(len(a)-1,-1,-1):
  b+=a[i]
if b==a:
  print("Yes its palindrone")
else:
  print("No its not a palindron")

