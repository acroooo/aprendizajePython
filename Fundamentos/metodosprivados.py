class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        # Tipos de restricciones para atributos
        # Publico
        self.nombre = nombre
        # Parcialmente privado / protegido
        self._ape_paterno = ape_paterno
        # Privado
        self.__ape_materno = ape_materno

    # Se puede llamandolo desde un metodo publico
    def metodo_publico(self):
        self.__metodo_privado()

    def __metodo_privado(self):
        print(self.nombre)
        print(self._ape_paterno)
        print(self.__ape_materno)

    def get_apellido_materno(self):
        return self.__ape_materno

    def set_apellido_materno(self, ape_materno):
        self.__ape_materno = ape_materno

p1 = Persona( "Juan", "Lopez", "Perez")
# No se puede acceder al metodo privado
#p1.__metodo_privado()

# Llamo metodo publico
p1.metodo_publico()

# accesos
print(p1.nombre)
print(p1._ape_paterno)
print(p1.get_apellido_materno())