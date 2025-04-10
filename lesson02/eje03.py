# conditional
nota=int(input("introduce tu nota del examen(10-100): "))
if(100>=nota>=90):
  print("Tienes un A")
elif(nota<90 and nota>=80):
  print("Tienes un B")
elif(80>nota>=70):
  print("Tienes un C")
elif(nota<70):
  print("Tienes un D")
else:
  print("Nota introducido invalido!!")