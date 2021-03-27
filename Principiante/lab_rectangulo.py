class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho


    def area(self):
        return self.ancho * self.alto


rectangulo = Rectangulo(13,20)
print(rectangulo.area())