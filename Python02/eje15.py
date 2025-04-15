""" Escribir un programa que solicite por teclado 10 notas de alumnos y nos
informe cuántos tienen notas mayores o iguales a 7 y cuántos menores. (tambien hecho antes con for ahora con while para practicar!!)"""
numAlumno=10
ContadorMayorIgual=0
ContadorMenor=0
i=1
while i<=numAlumno:
  nota=float(input("Introduce la nota: "))
  if nota>=7:
    ContadorMayorIgual+=nota
    continue
  ContadorMenor+=1
print(f"Numero total de alumons con nota mayor o igual que siete es {ContadorMayorIgual}")
print(f"Numero total de alumons con nota menor que siete es {ContadorMenor}")