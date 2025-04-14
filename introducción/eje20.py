"""  Se ingresan tres valores por teclado, si todos son iguales se imprime la
suma del primero con el segundo y a este resultado se lo multiplica por
el tercero."""
num1=int(input("Intoduce un número: "))
num2=int(input("Intoduce dos número: "))
num3=int(input("Intoduce tres número: "))
if num1==num2==num3:
  suma=num1+num2
  print(f"La suma del {num1} y {num2} es {suma}")
  print(f"La multiplicacion del {suma} y {num3} es {suma*num3}")
else:
  print("Los números son distintos")