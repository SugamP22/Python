""" Desarrollar un programa que permita la carga de 10 valores por teclado y nos
muestre posteriormente la suma de los valores ingresados y su promedio. Este
problema ya lo desarrollamos, lo resolveremos empleando la estructura for
para repetir la carga de los diez valores por teclado. (hecho antes con for ahora voy a hacer con while)"""
sumaCOntaodr=0
i=1
while i<=10:
  num=int(input("Introduce un numero: "))
  sumaCOntaodr+=num
  if i==10:
    break
  i+=1
promedio=sumaCOntaodr/i
print(f"La promedio de la suma total es {promedio}")
  