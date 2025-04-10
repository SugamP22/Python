# write a code to check if it contains palindrome of elements
list1=[1,2,3,2,1]
copyList1=list1.copy()
print(copyList1)
list1.reverse()
if (copyList1==list1):
  print("Si es un palindrome")
else:
  print("No, no es un palindrome!!")

