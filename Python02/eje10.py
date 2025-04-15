""" Desarrollar un programa que permita cargar n números enteros y luego nos
informe cuántos valores fueron pares y cuántos impares.
Emplear el operador “%” en la condición de la estructura condicional (este
operador retorna el resto de la división de dos valores, por ejemplo 11%2
retorna un 1): """
cantidad=int(input("Ingresa una cantidad de numeros: "))
contadorPar=0
contadorImpar=0
for i in range(1,cantidad):
 if i%2==0:
   contadorPar+=1
   continue
 contadorImpar+=1   
print(f"Numero pares encontrado dentro de primeros {cantidad} numeros son {contadorPar} ")
print(f"Numero Impares encontrado dentro de primeros {cantidad} numeros son {contadorImpar} ")