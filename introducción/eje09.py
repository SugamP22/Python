""" Se ingresan tres notas de un alumno, si el promedio es mayor o igual a
siete mostrar un mensaje "Promocionado" """
num=()
for i in range(1,4):
  num1=int(input("Intoduce un numero :"))
  num=num+(num1,)
promedio=(num[0]+num[1]+num[2])/len(num)
if(promedio>=7):
  print("Promocionado")
else:
  print("End")
