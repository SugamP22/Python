""" Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
cuántos tienen notas mayores o iguales a 7 y cuántos menores.
 """
alumnoENota={}
contadorMayor=0
contadoeMenor=0
numAlumno=int(input("Introduce numero de alumnos registrado: "))
for notaAlumno in range(1,numAlumno+1):
  nota=float(input(f"Introduce nota para alumno {notaAlumno}: "))
  alumnoENota[f"Alumno{notaAlumno}"]=nota
  if(nota<7):
    contadoeMenor+=1
  else:
    contadorMayor+=1
alumno=list(alumnoENota.keys())
nota=list(alumnoENota.values())
for i in range(0,len(alumnoENota)):
  if(nota[i]==7):
    print(f"{alumno[i]} tiene nota igual que siete( Nota = {nota[i]})")
  elif(nota[i]>7):
    print(f"{alumno[i]} tiene nota mayor  que siete( Nota = {nota[i]})")
  else:
    print(f"{alumno[i]} tiene nota menor que siete( Nota = {nota[i]})")
# print(alumnoENota)
print(f"Numero total de alumnos con nota mayor igual que siete es {contadorMayor}")
print(f"Numero total de alumnos con nota menor que siete es {contadoeMenor}")
