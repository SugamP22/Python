""" En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y
$500, realizar un programa que lea los sueldos que cobra cada empleado e
informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de
$300. Además el programa deberá informar el importe que gasta la empresa en
sueldos al personal.
 """
contadormenor=0
contadorMayor=0
numEmpleados=int(input("Ingresa numeros empleados trabajando en una empresa: "))
for i in range(1,numEmpleados+1):
  sueldo=int(input(f"Ingresa sueldo de {i} empleado: "))
  if sueldo<300:
    contadormenor+=1
    continue
  contadorMayor+=1
print(f"El numero de empleado con sueldo mayor que 300 son {contadorMayor}")
print(f"El numero de empleado con sueldo mayor que 300 son {contadormenor}")
