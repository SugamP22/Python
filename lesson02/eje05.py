# encontral el numero más grande
num1=float(input("Introduce primer numero: "))
num2=float(input("Introduce segundo numero: "))
num3=float(input("Introduce tercero numero: "))
if (num2<num1>num3):
  print(f"El numero {num1} es mayor que numero {num2} y {num3}")
elif(num1<num2>num3):
  print(f"El numero {num2} es mayor que numero {num1} y {num3}")
else:
  print(f"El numero {num3} es mayor que numero {num2} y {num1}")