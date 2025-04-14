""" Confeccionar un programa que permita cargar un número entero positivo
de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3
cifras. Mostrar un mensaje de error si el número de cifras es mayor """
num=int(input("Introduce un número: "))
if num>0 and num<1000:
  if num<10:
    print("Tiene 1 digito")
  elif num<100:
    print("Tiene 2 digito")
  else:
    print("Tiene 3 digito")
else:
  print("Entrada inválido")
  
    
  