""" Confeccionar un programa que lea n pares de datos, cada par de datos
corresponde a la medida de la base y la altura de un triángulo. El programa
deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12. """
n=10
triangulos=[]
contadorSuferficia=0
for i in range(1,n+1):
  print(f"======= Ronda {i} ========")
  datobase=float(input(f"Introduce la base de triangulo {i}: "))
  datoaltura=float(input(f"Introduce la altura de triangulo {i}: "))
  superficie=(datoaltura*datobase)/2
  if(superficie>12):
    contadorSuferficia+=1
  info={
   "Triangulo": i,
    "Base":datobase,
        "Altura":datoaltura,
       "Superficie":superficie}
  triangulos.append(info)
for t in triangulos:
    for clave, valor in t.items():
        print(f"{clave}: {valor}")
    print("-----------------")
print(f"Numero total de triángulos cuyos superficie es mayor que 12 es {contadorSuferficia}")