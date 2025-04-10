# comprobar si el numero introducido es un multiplo de 7 o no?
num=int(input("Introduce un numero: "))
if(num % 7 == 0):
  print(f"El numero {num} es un multiplo de 7")
else:
  print(f"El numero {num} no es un multiplo de 7")