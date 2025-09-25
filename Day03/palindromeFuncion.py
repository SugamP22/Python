def palindromeWord(name):
  reverse=""
  for i in range(len(name)-1,-1,-1):
   reverse+=name[i]
   
  if(reverse==name):
    print("Yes its a palindronme")
  else:
   print("No , its not a palindrome")
   


palindromeWord("naman")
palindromeWord("sugam")