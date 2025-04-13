dict={}
list=[input("introduce sujeto :"),input("introduce sujeto: "),input("introduce un sujeto: ")]
dict[list[0]]=int(input(f"Introduce la nota que has obtenido en {list[0]}: "))
dict[list[1]]=int(input(f"Introduce la nota que has obtenido en {list[1]}: "))
dict[list[len(list)-1]]=int(input(f"Introduce la nota que has obtenido en {list[len(list)-1]}: "))
print(dict)