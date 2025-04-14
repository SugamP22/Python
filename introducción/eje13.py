""" Se ingresa por teclado un valor entero, mostrar una leyenda que indique
si el número es positivo, negativo o nulo (es decir cero) """

num=int(input("Introduce un numero: "))
if num<0:
  print("Numero introducido es negativo")
elif num==0:
  print("Numero introducido es nulo")
else:
  print("Numero introducido es positivo")
 

