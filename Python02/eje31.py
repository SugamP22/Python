""" Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un
caracter "@"
Para analizar cada caracter del string ingresado disponemos una estructura
while utilizando un contador llamado x que comienza con el valor cero y se
repetirá tantas veces como caracteres tenga la cadena (mediante la función len
obtenemos la cantidad de caracteres):
"""
nombre="sugam@gmail.com"
contadorAt=0
x=0
while x<len(nombre):
  if nombre[x]=='@':
    contadorAt+=1
  x+=1
  
if contadorAt>1:
  print("ERROR: invalido")
else:
  print("Valido!!")