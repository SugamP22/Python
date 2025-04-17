""" Realizar la carga por teclado del nombre, edad y altura de dos personas.
Mostrar por pantalla el nombre de la persona con mayor altura. """
for i in range(1,3):
  print(f"===== Persona {i} =====")
  nombre=input("Introduce un nombre: ")
  edad=int(input("Ingresa tu edad: "))
  if(i==1):
   alturaPrimerPersona=float(input("Ingresa tu altura: "))
  else:
   alturasegundaPersona=float(input("Ingresa tu altura: "))
if(alturaPrimerPersona>alturasegundaPersona):
  print("La altura de persona uno es mayor que la segunda persona!!")
else:
  print("La altura de segunda persona es mayor que la primera persona!!")  
    