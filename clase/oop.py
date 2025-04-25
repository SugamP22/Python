class Persona:
    def __init__(self, nombre, apellidos, ciudad, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.ciudad = ciudad
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Teléfono: {self.telefono}")


nombre=input("Ingresa un nombre: ")
Apellido=input("Ingresa un nombre: ")
Ciudad=input("Ingresa un nombre: ")
telefonon=int(input("Ingresa tu numero telefono: "))
persona1 = Persona(nombre,Apellido,Ciudad,telefonon)
persona1.mostrar_info()
