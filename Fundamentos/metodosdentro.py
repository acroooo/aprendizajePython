class Aritmetica:
    """
    Clase aritmética para realizar operaciones de sumar, restar, etc
    """
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def sumar(self):
        """
        Se realiza la operacion con los atributos de la clase
        """
        return self.op1 + self.op2

# CREAMOS UN NUEVO OBJETO
aritmetica = Aritmetica(10, 28)

print("Resultado suma: ", aritmetica.sumar())