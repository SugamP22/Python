""" Codificar un programa que lea n números enteros y calcule la cantidad de
valores mayores o iguales a 1000 (n se carga por teclado)
Este tipo de problemas también se puede resolver empleando la estructura
repetitiva for. Lo primero que se hace es cargar una variable que indique la
cantidad de valores a ingresar. Dicha variable se carga antes de entrar a la
estructura repetitiva for. """
contadorMayor=0
cantidadNumeros=int(input("Introduce la cantidad de numeros enteros para introducir ::> "))
for i in range(1,cantidadNumeros+1):
  num=int(input(f"Introducir valor para posicion {i} ::>"))
  if num>=1000:
    contadorMayor+=1
    continue
print(f"Numero total de numeros mayor igual que 1000 es {contadorMayor}")
  