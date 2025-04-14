numtuple=(1,4,9,16,25,36,49,64,81,100)
num=int(input("Introduce un numero para encontrar: "))
encontrado=False
count=1
while (not encontrado and count!=len(numtuple)):
  if(numtuple[count-1]==num):
    encontrado=True
    position=count
    break
  count+=1
  
if(encontrado):
  print(f"Encontrado en posición {position}")
else:
  print("No hemos podido lograr este número!!")