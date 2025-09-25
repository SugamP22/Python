import random
number=random.randint(1,10)
count=1
while True:
  print(f"-------- Turno {count} ------ ")
  guess=int(input("Enter your guess(1-10): "))
  if(guess==number):
    print("Your guess is correct!!")
    break
  elif guess>number:
    print("Go lower")
  elif guess<number:
    print("Go higher")
  else:
    print("Your guess is not correct!!")
    count+=1

print(f"You were able to guess the number total numbe of guess were {count}")
