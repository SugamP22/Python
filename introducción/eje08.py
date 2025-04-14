"""  Realizar un programa que solicite la carga por teclado de dos números,
si el primero es mayor al segundo informar su suma y diferencia, en
caso contrario informar el producto y la división del primero respecto al
segundo """

num1=float(input("Introduce número:"))
num2=float(input("Introduce número:"))
if(num1>num2):
  print(f"Suma = {num1+num2}")
  print(f"Diferencia = {num1-num2}")
else:
  print(f"Diferencia = {num1*num2}")
  print(f"Diferencia = {num1/num2}")
  