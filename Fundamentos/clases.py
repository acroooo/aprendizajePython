class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Ejemplo:
    pass
# MODIFICAR VALORES
Persona.nombre = "Juan"
Persona.edad = 28
# ACCEDER A LOS VALORES
print(Persona.nombre)
print(Persona.edad)
print(Ejemplo)

# CREACION DE UN OBJETO
persona = Persona("Karla", 30)

# CREACION DE UN SEGUNDO OBJETO
persona2 = Persona("Hernan", 31)

print(persona2.nombre)

print(id(persona))
print(persona)