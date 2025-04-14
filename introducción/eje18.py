""" Se ingresan por teclado tres números, si todos los valores ingresados
son menores a 10, imprimir en pantalla la leyenda "Todos los números
son menores a diez". """
num1=int(input("Numero uno: "))
num2=int(input("Numero Dos: "))
num3=int(input("Numero Tres: "))
if num1 < 10 and num2 < 10 and num3< 10:
  print("Todos los numeros son menor de 10")
else:
  print("Has equivocado algunos son mayores de 10")
