""" Escribe un programa en Python que pida al usuario cuántos valores va a
ingresar. Luego, solicita esos valores uno por uno y al final muestra cuántos
números negativos se ingresaron.
 """
cantidad=int(input("Introducir la cantidad numeros qe deseas trabajar con::> "))
contarNumerosNegativo=0
for i in range(1,cantidad+1):
  num=int(input(f"Introducir numero {i} ::>")) 
  if num<0:
    contarNumerosNegativo+=1
print(f"Numeros negativo introducido es {contarNumerosNegativo}")