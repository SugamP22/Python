""" Se cargan por teclado tres números distintos. Mostrar por pantalla el
mayor de ellos.
 """
 
num1=float(input("Introduce numero uno: "))
num2=float(input("Introduce numero dos: "))
num3=float(input("Introduce numero tres: "))
if num3< num1 > num2:
  print(f"{num1} es mayor que {num2} e {num3}")
elif num3< num2 > num1:
  print(f"{num2} es mayor que {num1} e {num3}")
else:
  print(f"{num3} es mayor que {num1} e {num2}")