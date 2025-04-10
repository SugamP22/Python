# write a code to check if it contains palindrome of elements
list=[1,"abc","abc",2]
listCopy=list.copy()
list.reverse()
if(list==listCopy):
  print("Es un palindrome")
else:
  print("No es un palindrome")