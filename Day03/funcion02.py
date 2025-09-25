def division(number,num):
  return number//num
def sum(number,num):
  return number+num

def hello(name,age=1):
  print(f"Name : {name} and Age : {age}")

def substract(a,b=10):
  return b-a
  
number=int(input("Enter a number: "))
number1=int(input("Enter a number: "))
print(f"The result after dividing both number is {division(number,number1)}")
print(f"The result after adding both number is {sum(number,number1)}")
hello("sugam")
hello(age=10,name="sugam")