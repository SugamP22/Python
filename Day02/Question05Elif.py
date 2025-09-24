temp=int(input("Enter a temperature in celcius: "))
if temp<0:
  print("Freezing cold!!")
elif temp>0 and temp<=10:
  print("Very cold")
elif temp>10 and temp<=20:
  print("Cold!!")
elif temp>20 and temp<=30:
  print("Pleasent")
elif temp>30 and temp<=40:
  print("Hot")
else:
  print("Very Hot!!")