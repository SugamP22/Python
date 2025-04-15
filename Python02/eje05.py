""" Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura
promedio de las personas.
 """
sumaAlturas=0
numPersonas=int(input("Introduce numeros de personas: "))
for idx in range(1,numPersonas+1):
  altura=float(input(f"Introduce altura de {idx} persona: "))
  sumaAlturas+=altura
  
print(f"La promedio de alturas introducido es {sumaAlturas/numPersonas}")