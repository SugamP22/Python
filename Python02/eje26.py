""" Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un
promedio de edades mayor.
 """
sumaManiana=0
sumaTarde=0
sumaNoche=0
for i in range(1,23):
  if(i<6):
    print(f"===== Turno mañana Estudiante {i} ======")
    estudiante=int(input("Ingresa la edad: "))
    sumaManiana+=estudiante
  elif(i<12):
    print(f"===== Turno Tarde Estudiante {i} ======")
    estudiante=int(input("Ingresa la edad: "))
    sumaTarde+=estudiante
  else:
    print(f"===== Turno Noche Estudiante {i} ======")
    estudiante=int(input("Ingresa la edad: "))
    sumaNoche+=estudiante
promedioManiana=sumaManiana/5
promedioTarde=sumaTarde/6
promedioNoche=sumaNoche/11
print(f"El promedio de turno Mañana: {promedioManiana}")
print(f"El promedio de turno Tarde: {promedioTarde}")
print(f"El promedio de turno Noche: {promedioNoche}")
if promedioNoche<promedioManiana>promedioTarde:
  print("Promedio de turno mañana es mayor que otros")
elif promedioManiana<promedioTarde>promedioNoche:
  print("Promedio de turno Tarde es mayor que otros")
else:
  print("Promedio de turno Noche es mayor que otros")
  

    