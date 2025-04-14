num=[4,9,16,25,36,49,64,81,100]
numPaEncontrar=int(input("Introduce un numero: "))
encontrado=False
idx=1
for value in num:
  if(value!=numPaEncontrar):
    idx+=1
    continue
  else:
    encontrado=True
    break
if(encontrado):
     print(f"Hemos podido lograr el numero {numPaEncontrar} en posición {idx} con exitó !!")
else:
     print("No hemos podido lograr esa numero!!")
