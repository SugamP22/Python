# # en este aprendimos sobre tuple enm list podriamos cambiar los valores(assigment is not allowed) pero en tuple no una vez creado no se puede cambiar los valores se crear dentro de ()
# name="hello world"
# in string i could replca but i will not affect the originalk form i need to create a new variable to store it
# print(name.replace("l", "y"))
# print(name)
tup=(10,11,12,13,14,15,12,12)
print(tup.index(11))
print(tup.count(12))
print(tup[:len(tup)])
tup2=(1,)
print(type(tup2))
tup3=(1)
print(type(tup3))
# u must use  a comma with a single value if not the programm will not get the difference between tupple and other variable