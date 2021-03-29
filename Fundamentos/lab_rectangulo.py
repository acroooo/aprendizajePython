class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho


    def area(self):
        return self.ancho * self.alto


# Pido datos
base = int(input("Proporcione la base: "))
altura = int(input("Proporcione la altura: "))

rectangulo = Rectangulo(base, altura)
print(rectangulo.area())