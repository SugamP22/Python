""" Busca en internet como realizar el IMC índice de masa corporal y realiza un
programa que lo calcule, me tendrá que pedir el peso y la estatura. """
altura=float(input("Introduce una altura corporal: "))
peso=float(input("Introduce la masa corporal: "))
res=peso/(altura*altura)
print(f"La IMC con altura {altura} y peso {peso} es {res}")