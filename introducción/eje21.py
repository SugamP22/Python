""" Escribir un programa que pida ingresar la coordenada de un punto en el
plano, es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante se ubica dicho
punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
 """
x=int(input("Ingresa la cordinada de punto x: "))
y=int(input("Ingresa la cordinada de punto Y: "))
if(x>0 and y >0):
  print("Esta ubicada en primer cuadrante")
elif(x<0 and y <0):
  print("Esta ubicada en segundo cuadrante")
elif(x>0 and y <0):
  print("Esta ubicada en tercer cuadrante")
else:
  print("Esta ubicada en cuarta cuadrante")