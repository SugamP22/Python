""" Escribir un programa que lea 10 números enteros y luego muestre cuántos
valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en
cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
 """
contadorAmbos=0
contadorTres=0
contadorCinco=0
contadorOtros=0
for idx in range(1,11):
  num=int(input(f"Introduce numero {idx} ::> "))
  if num%3==0 and num%5==0 :
    contadorAmbos+=1
  elif num%3==0:
    contadorOtros+=1
  elif num%5==0:
    contadorCinco+=1
  else:
    contadorOtros+=1
print(f"Numero total de multiplos de ambos 3 y 5 es {contadorAmbos}")
print(f"Numero total de multiplos de ambos 3 es {contadorTres}")
print(f"Numero total de multiplos de  5 es {contadorCinco}")
print(f"Numero total de multiplos de  otros numeros es {contadorOtros}")
  