""" Se ingresan por teclado tres números, si al menos uno de los valores
ingresados es menor a 10, imprimir en pantalla la leyenda "Alguno de los
números es menor a diez".
 """
num=int(input("Ingresa un número: "))
num2=int(input("Ingresa un número: "))
num3=int(input("Ingresa un número: "))
if(num<10 and num2<10 and num3<10):
  print("Todos numeros son menores de 10")
elif(num<10 or num2<10 or num3<10):
  print("Alguno de estos son menores de 10 ")
else:
  print("Ninguno de los numeros son menores de 10")
  