""" Escribir un programa en el cual: dada una lista de tres valores numéricos
distintos se calcule e informe su rango de variación (debe mostrar el
mayor y el menor de ellos)
 """
num1=int(input("Ingresa numero uno:"))
num2=int(input("Ingresa numero dos: "))
num3=int(input("Ingresa numero tres: "))
if(num1==num2==num3) or num1==num2 or num1==3:
  print("Hay numeros comunes!!")
elif(num1>2 & num1>num3):
  print(f"{num1} es mayor igual que {num2} e {num3}")
elif(num2>1 & num2>num3):
  print(f"{num2} es mayor igual que {num1} e {num3}")
else:
  print(f"{num3} es mayor igual que {num1} e {num2}")
  