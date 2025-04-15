""" Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de piezas
a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza
cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir
por pantalla la cantidad de piezas aptas que hay en el lote.
 """
aptoOno=[]
hierro={}
num=int(input("Ingresa el numeros de piezas: "))

for i in range(1,num+1):
  longitude=float(input(f"Ingresa la longitude de pieza {i}: "))#ahora lo que hacemos una lista donde guardamos si es apta o no comparando en esa loop
  hierro[f"posicion{i}"]=longitude
  if(longitude>=1.20 and longitude<=1.30):
    aptoOno.append("apto")
  else:
    aptoOno.append("noapto")
print(hierro)
for idx in range(0,len(aptoOno)):
  if(aptoOno[idx]=="apto"):
    print(f"la pieza in la posicion {idx+1} es apto")
  
  
  