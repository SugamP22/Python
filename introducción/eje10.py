""" Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un
número entero)
 """
num=int(input("Introduce un numero: "))
if 100>= num>=1:
  if num<=10:
    print("El numero introducido tiene 1 digito!!")
  elif num<100:
    print("El numero ingresado tiene 2 digitos!!")
  else:
    print("El numero ingresado tiene 3 digitos!!")
    
else:
  print("Entrada inválido!!")