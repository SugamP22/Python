""" Desarrollar un programa que solicite la carga de 10 números e imprima la suma
de los últimos 5 valores ingresados """
sumaUltimas5=0
for i in range(1,11):
  num=int(input(f"Introduce numero {i} ::>"))
  if(i>=5):
    sumaUltimas5+=num
print(f"La suma de los 5 ultimos numeros es {sumaUltimas5}")