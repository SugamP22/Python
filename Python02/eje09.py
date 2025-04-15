""" Realizar un programa que permita cargar dos listas de 15 valores cada una.
Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un
algoritmo.
 """
listUno=[]
listaDos=[]
for i in range(1,16): 
 print(f"*** ronda {i} ***")
 numPaUno=float(input(f"Introduce valor para lista Uno:"))
 numPaDos=float(input(f"Introduce valor para lista Dos:"))
 listUno.append(numPaUno)
 listaDos.append(numPaDos)
print(listUno)
print(listaDos)
sumaUno=sum(listUno)
sumaDos=sum(listaDos)
if(sumaUno==sumaDos):
  print(f"Las listas son iguales (Suma = {sumaUno})")
elif(sumaUno>sumaDos):
  print(f"Lista uno es mayor (Suma lista Uno = {sumaUno}, suma lista Dos {sumaDos})")
else:
  print(f"Lista dos es mayor (Suma lista Uno = {sumaUno}, suma lista Dos {sumaDos})")
