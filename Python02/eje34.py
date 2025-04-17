# Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se
# ingresaron. Tener en cuenta que un espacio en blanco es igual a
# " ", en cambio una cadena vacía es ""
# oracion="hello my name is sugam, how u doin?"
oracion=" "
contadorEspacio=0
if oracion=="":
  print("ERROR: Inválido!!")
else:
  for i in range(0, len(oracion)):
    if(oracion[i]==" "):
      contadorEspacio+=1
  print(f"La cantidad de espacios en [{oracion}] es {contadorEspacio}")
      