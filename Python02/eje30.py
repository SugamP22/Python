""" Solicitar la carga del nombre de una persona en minúsculas. Mostrar un
mensaje si comienza con vocal dicho nombre.
 """
nombre="SUGAM"
print(nombre)
print(f"En miniscula {nombre.lower()}")
if nombre[0].lower() in ['a','e','i','o','u']:
  print("si empieza con vocal")
else:
  print("No, no empieza con ningun vocal!!")