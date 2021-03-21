class Persona:
    def __init__(self, n):
        self.__nombre = n
        # podemos crear atributos sin argumentos
        self.__edad = 28

    # Leo el atributo
    def get_nombre(self):
        return self.__nombre

    # Seteo el atributo
    def set_nombre(self, nombre):
        self.__nombre = nombre

    #edad
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad

p1 = Persona("Juan")
# Leo la informacion
print(p1.get_nombre())
p1.set_nombre("Hernán")
print(p1.get_nombre())