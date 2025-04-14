numeros=()
for i in range(1,5):
 nuevonum=int(input("Introduce un numero: "))
 numeros=numeros+(nuevonum,)
res=numeros[0]+numeros[1]+numeros[2]+numeros[3]
print(f"La suma de numeros {numeros} es {res}\nLa promedio de numeros {numeros} es {res/len(numeros)}")