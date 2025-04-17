""" Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
 """
contadorMultiplo=0
contadorNegativo=0
contadorPositivo=0
sumaPares=0
for i in range(1,11):
   print(f"======== Número {i} ==========")
   num=int(input("Ingresa un numero::> "))
   if num<0 :
      contadorNegativo+=1
   if num>0:
      contadorPositivo+=1
   if num % 15 ==0 :
      contadorMultiplo+=1
   if num %2 ==0:
      sumaPares+=num
print(f"La cantidad total de valores negativos ingresado por usuario es {contadorNegativo}")
print(f"La cantidad total de valores positivos ingresado por usuario es {contadorPositivo}")
print(f"La cantidad total de cantidad de nultiplo de 15 ingresado por usuario es {contadorMultiplo}")
print(f"El valor acumulado de los numeros  ingresado por usuario que son pares es {sumaPares}")