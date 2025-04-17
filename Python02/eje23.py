""" Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
 """
triangulos=int(input("Ingresa la cantidad de triangulos: "))
for t in range(1,triangulos+1):
  print(f"====== Triangulo {t} =======")
  num1=float(input("Ingresa Altura: "))
  num2=float(input("Ingresa base: "))
  num3=float(input("Ingresa curva: "))
  if(num1==num2==num3):
    print("Es un triangulo equilátero")
  elif(num2==num1) or (num3==num2) or (num1==num3):
    print("Es un triangulo isósceles")
  else:
    print("Es un triangulo escaleno")
  print("__________________________")
  print(f"Altura: {num1}\nBase: {num2}\nCurva: {num3}")