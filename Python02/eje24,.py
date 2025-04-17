""" Escribir un programa que pida ingresar coordenadas (x,y) que representan
puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad
de puntos a procesar.
 """
contadorPrimero=0
contadorSegundo=0
contadorTercero=0
contadorCuarto=0
cantidadPuntos=int(input("Ingresar cantidad de puntos con que quieres trabajar::> "))
for punto in range(1,cantidadPuntos+1):
  print(f"========== Punto {punto} ==========")
  x=float(input("Ingresa el punto en eje-x::> ")) 
  y=float(input("Ingresa el punto en eje-y::> "))
  print("******************************")
  if(x>0 and y >0):
    contadorPrimero+=1
    print("Esta ubicado en primer cuadrante")
  elif(x<0 and y>0):
    contadorSegundo+=1
    print("Esta ubicado en segundo cuadrante")
  elif(x<0 and y<0):
    contadorTercero+=1
    print("Esta ubicado en tercer cuadrante")
  else:
    contadorCuarto+=1
    print("Esta ubicado en cuarto cuadrante")
  print("******************************")
print(f"Puntos ubicado en primer Cuadrante es {contadorPrimero}")
print(f"Puntos ubicado en segundo Cuadrante es {contadorSegundo}")
print(f"Puntos ubicado en tercero Cuadrante es {contadorTercero}")
print(f"Puntos ubicado en cuarto Cuadrante es {contadorCuarto}")