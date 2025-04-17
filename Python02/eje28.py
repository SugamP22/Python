""" Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es
mayor alfabéticamente o si son iguales. """
for i in range(1,3):
  print(f"====== Persona {i} ========")
  if(i==1):
    nombrePrimerPersona=input("Introduce tu nombre: ")
  else:
    nombreSegundoPersona=input("Introduce tu nombre: ")
if(nombrePrimerPersona>nombreSegundoPersona):
  print("La nombre primer persona es mayor alfabeticamente")
elif(nombreSegundoPersona>nombrePrimerPersona):
  print("La nombre segunda persona es mayor alfabeticamente")
else:
  print("Ambos son iguales")
  
    