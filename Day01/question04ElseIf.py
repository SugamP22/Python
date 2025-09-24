name=input("Please enter your name: ").lower()
age=int(input("Please enter your age: "))
if age>=18 and age<100:
  print(f"Yes, {name} you can cast vote being {age} year old")
elif age<18:
  print(f"No, {name} you cannot cast vote being {age} year old")
else:
  print("You age is invalid!!")
  