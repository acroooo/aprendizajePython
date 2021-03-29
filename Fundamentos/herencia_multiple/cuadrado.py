from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # por orden de prioridad llama al que primero este dentro de los atributos, si lo llamo con super
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho