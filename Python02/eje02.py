""" Desarrollar un programa que permita la carga de 10 valores por teclado y nos
muestre posteriormente la suma de los valores ingresados y su promedio.
 """
num=()
suma=0
for turno in range(1,11):
   num=num+(int(input(f"Ingresa {turno} numero: ")),)
for idx in range(0,len(num)):
 suma+=num[idx]
promedio=suma/len(num)
print(f"La suma de {num} es suma {suma}")
print(f"La promedio de la suma es {promedio}")
 