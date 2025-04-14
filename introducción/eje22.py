""" De un operario se conoce su sueldo y los años de antigüedad. Se pide
confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10
años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años,
otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
cambios. """
sueldo=float(input("Introuduce sueldo : "))
anios=int(input("Introuduce años de antigúedad : "))
sueldoAPagar=0
if(sueldo<500 and anios>=10):
  sueldoAPagar=sueldo+(sueldo*0.2)
elif(sueldo<500 and anios<10):
  sueldoAPagar=sueldo+(sueldo*0.05)
elif(sueldo>=500):
  sueldoAPagar=sueldo
else:
  print("Entrada invalido")
print(f"El sueldo al pagar es {sueldoAPagar}")