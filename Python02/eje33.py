# Ingresar una oración que pueden tener letras tanto en mayúsculas como
# minúsculas. Contar la cantidad de vocales. Crear un segundo string con toda la
# oración en minúsculas para que sea más fácil disponer la condición que verifica
# que es una vocal.
nombre="AuGam"
sugamENMini=nombre.lower()
cantidadVocales=0
for i in range(0,len(sugamENMini)-1):
  if sugamENMini[i] in ['a','e','i','o','u']:
    cantidadVocales+=1
print(f"Numero de vocales in {nombre} es {cantidadVocales}")