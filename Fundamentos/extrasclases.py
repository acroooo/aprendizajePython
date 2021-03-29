class Persona:
    # Se pueden pasar tuplas
    def __init__(this, nombre, edad, *v):
        this.nombre = nombre
        # CREO EL ATRIBUTO DE LA CLASE CON EL VALOR DEL ARGUMENTO DE LA CLASE
        this.edad = edad
        # TUPLA
        this.valores = v

p1 = Persona("Juan", 28)
print(p1.nombre)
print(p1.edad)

p2 = Persona("Karla", 30, 2,4,5)
print(p2.valores)