""" Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 -
24, etc  """
valor=0
i=1
while valor<500:
  multi=8*i
  print(multi)
  valor=multi
  i+=1
if(valor==500):
  print(f"Hemos legado justo a  500 en posicion {i}")
else:
  print(f"Hemos superado justo a  500 en posicion {i}")
 
    
