
# CLASE PADRE
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # redefino el metodo que se debe ejecutar (print)
    def __str__(self):
        # tengo que transformar en str para poder crear la cadena
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)


# CLASE HIJA
class Empleado(Persona):
    # Recibo de nuevo los parametros de la clase padre
    def __init__(self, nombre, edad, sueldo):
        # palabra reservada super para acceder a la clase padre ( metodos y atributos )
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    # SOBREESCRITURA DE STR
    def __str__(self):
        # reutilizo para no tener que retornar de nuevo
        return super().__str__() + ", sueldo: " + str(self.sueldo)


persona = Persona("Hernan", 28)
# directamente ejecuto ya que modifique el metodo que se debe ejecutar
print(persona)

empleado = Empleado("Juan", 30, 500.00)

print(empleado)

empleado.nombre = "carla Ivonn"
empleado.sueldo = 800.00

print(empleado)