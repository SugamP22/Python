""" Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos
muestre la tabla de multiplicar del mismo (los primeros 12 términos)
Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el
36.
 """
num=int(input("Ingresa un valor de uno a 10 : "))
for i in range(1,13):
  print(f"{num} x {i} = {num*i}")