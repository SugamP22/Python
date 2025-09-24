year=int(input("Enter to check if its a leap year: "))
if (year%100!=0 and year%4==0) or year%400==0:
  print(f"Yes, the year {year} is a leap year!!")
else:
  print(f"No, the year {year} is not a leap year!!")
  